import time
import torch
import torch.optim as optim
import numpy as np

from Hyperalignment.GPUHA import GPUHA
from Network.MLP import MLP

class DHA:
    def __init__(self, net_shape, activation, loss_type='mse', optim='sgd', iteration=10, epoch=10, learning_rate=0.1, regularization=10**-4, best_result_enable=True, gpu_enable=torch.cuda.is_available()):

        assert len(net_shape) > 0, "Model must have at least one layer!"
        assert len(activation) > 0, "Please enter the activation function"
        if len(activation) != 1:
            assert len(net_shape) == len(activation), "Length of the model and the list of activation functions are not matched!"

        assert int(iteration) > 0, "Iteration must be grater than 0"

        assert int(epoch) > 0, "Epoch must be grater than 0"

        assert float(regularization) > 0, "Regularization must be grater than 0"

        assert float(learning_rate) > 0, "Learning rate must be grater than 0"

        assert str.lower(optim) == 'adam' or str.lower(optim) == 'sgd', "Optimization algorithm is wrong!"


        assert str.lower(loss_type) == 'norm' or str.lower(loss_type) == 'mean' or str.lower(loss_type) == 'soft' or \
               str.lower(loss_type) == 'mse', "Loss type is wrong!"


        self.best_result_enable = best_result_enable
        self.net_shape = net_shape
        self.activation = activation
        self.iteration = int(iteration)
        self.epoch = int(epoch)
        self.learning_rate = float(learning_rate)
        self.regularization = float(regularization)
        self.gpu_enable = gpu_enable
        self.loss_type = str.lower(loss_type)
        self.optim = str.lower(optim)
        self.Share = None
        self.ha_loss_vec = None
        self.ha_loss = None
        self.ha_loss_test_vec = None
        self.ha_loss_test = None
        self.TrainFeatures = None
        self.TrainRuntime = None
        self.TestFeatures = None
        self.TestRuntime = None



    def train(self, views, verbose=True):
        tic = time.time()
        assert len(np.shape(views)) == 3, "Data shape must be 3D, i.e. sub x time x voxel"

        self.Share = None
        self.TrainFeatures = None

        NumSub, NumTime, NumVoxel = np.shape(views)
        NumFea = self.net_shape[-1]
        if NumFea is None:
            NumFea = np.min((NumTime, NumVoxel))
            if verbose:
                print("Number of features is automatically assigned, Features: ", NumFea)
                self.net_shape[-1] = NumFea

        Share = np.random.randn(NumTime, NumFea)

        if   self.loss_type == 'mse':
            criterion = torch.nn.MSELoss()
        elif self.loss_type == 'soft':
            criterion = torch.nn.MultiLabelSoftMarginLoss()
        elif self.loss_type == 'mean':
            criterion = torch.mean
        elif self.loss_type == 'norm':
            criterion = torch.norm
        else:
            raise Exception("Loss function type is wrong! Options: \'mse\', \'soft\', \'mean\', or \'norm\'")

        self.ha_loss_vec = list()

        self.ha_loss = None

        for j in range(self.iteration):

            NewViews = list()
            G = torch.Tensor(Share)

            for s in range(NumSub):
                net_shape = np.concatenate(([NumVoxel], self.net_shape))
                net = MLP(model=net_shape, activation=self.activation, gpu_enable=self.gpu_enable)

                if self.optim == "adam":
                    optimizer = optim.Adam(net.parameters(), lr=self.learning_rate)
                elif self.optim == "sgd":
                    optimizer = optim.SGD(net.parameters(), lr=self.learning_rate)
                else:
                    raise Exception("Optimization algorithm is wrong! Options: \'adam\' or \'sgd\'")


                X = torch.Tensor(views[s])
                net.train()

                for epoch in range(self.epoch):
                    # Send data to GPU
                    if self.gpu_enable:
                        X = X.cuda()
                        G = G.cuda()

                    optimizer.zero_grad()
                    fX = net(X)

                    if self.loss_type == 'mse' or self.loss_type == 'soft':
                        loss = criterion(fX, G) / NumTime
                    else:
                        loss = criterion(fX - G) / NumTime

                    loss.backward()
                    optimizer.step()
                    sum_loss = loss.data.cpu().numpy()

                    if verbose:
                        print("TRAIN, UPDATE NETWORK: Iteration {:5d}, Subject {:6d}, Epoch {:6d}, loss error: {}".format(j+1, s+1, epoch+1, sum_loss))

                NewViews.append(net(X).data.cpu().numpy())

            ha_model = GPUHA(Dim=NumFea, regularization=self.regularization)

            if NumFea >= NumTime:
                ha_model.train(views=NewViews, verbose=verbose, gpu=self.gpu_enable)
            else:
                ha_model.train(views=NewViews, verbose=verbose, gpu=False)

            Share = ha_model.G
            out_features = ha_model.Xtrain
            error = np.mean(ha_model.Etrain)

            if   error == 0:
                assert self.Share is not None, "All extracted features are zero, i.e. number of features is not enough for creating a shared space"
                self.TrainRuntime = time.time() - tic
                return self.TrainFeatures, self.Share

            if self.best_result_enable:
                if self.ha_loss is None:
                    self.Share = Share
                    self.TrainFeatures = out_features
                    self.ha_loss = error

                if error <= self.ha_loss:
                    self.Share = Share
                    self.TrainFeatures = out_features
                    self.ha_loss = error
            else:
                self.Share = Share
                self.TrainFeatures = out_features
                self.ha_loss = error

            if verbose:
                print("Hyperalignment error: {}".format(error))

            self.ha_loss_vec.append(error)

        self.TrainRuntime = time.time() - tic
        return self.TrainFeatures, self.Share




    def test(self, views, TrainShare=None, verbose=True):
        tic = time.time()
        assert len(np.shape(views)) == 3, "Data shape must be 3D, i.e. sub x time x voxel"

        self.TestFeatures = None

        NumSub, NumTime, NumVoxel = np.shape(views)
        NumFea = self.net_shape[-1]
        if NumFea is None:
            NumFea = np.min((NumTime, NumVoxel))
            if verbose:
                print("Number of features is automatically assigned, Features: ", NumFea)
                self.net_shape[-1] = NumFea

        if TrainShare is not None:
            Share = TrainShare
            self.Share = TrainShare
        elif self.Share is not None:
            Share = self.Share


        if   self.loss_type == 'mse':
            criterion = torch.nn.MSELoss()
        elif self.loss_type == 'soft':
            criterion = torch.nn.MultiLabelSoftMarginLoss()
        elif self.loss_type == 'mean':
            criterion = torch.mean
        elif self.loss_type == 'norm':
            criterion = torch.norm
        else:
            raise Exception("Loss function type is wrong! Options: \'mse\', \'soft\', \'mean\', or \'norm\'")

        self.ha_loss_test_vec = list()
        self.ha_loss_test = None

        NewViews = list()
        G = torch.Tensor(Share)

        for s in range(NumSub):
            net_shape = np.concatenate(([NumVoxel], self.net_shape))
            net = MLP(model=net_shape, activation=self.activation, gpu_enable=self.gpu_enable)


            if self.optim == "adam":
                optimizer = optim.Adam(net.parameters(), lr=self.learning_rate)
            elif self.optim == "sgd":
                optimizer =  optim.SGD(net.parameters(), lr=self.learning_rate)
            else:
                raise Exception("Optimization algorithm is wrong! Options: \'adam\' or \'sgd\'")


            X = torch.Tensor(views[s])
            net.train()

            for j in range(self.iteration):
                # Send data to GPU
                if self.gpu_enable:
                    X = X.cuda()
                    G = G.cuda()

                optimizer.zero_grad()
                fX = net(X)

                if self.loss_type == 'mse' or self.loss_type == 'soft':
                    loss = criterion(G, fX)
                else:
                    loss = criterion(G - fX)

                loss.backward()
                optimizer.step()
                sum_loss = loss.data.cpu().numpy()

                if verbose:
                    print("TEST, UPDATE NETWORK: Iteration {:6d}, Subject {:6d}, loss error: {}".format(j+1, s+1, sum_loss))

            if self.gpu_enable:
                X = X.cuda()

            NewViews.append(net(X).data.cpu().numpy())

        ha_model = GPUHA(Dim=NumFea, regularization=self.regularization)
        ha_model.test(views=NewViews, G=Share, verbose=verbose)
        self.TestFeatures = ha_model.Xtest
        self.TestRuntime = time.time() - tic
        return self.TestFeatures


if __name__ == "__main__":
    data = np.random.rand(10, 10, 100)
    dat = np.random.rand(2, 10, 100)

    model = DHA([None], [None])
    model.train(data)
    model.test(dat)
    X = model.TrainFeatures
    Y = model.TestFeatures
    G = model.Share


    model1 = GPUHA()
    tic = time.time()
    model1.train(data)
    toc = time.time() - tic
    model1.test(dat)
    X2 = model1.Xtrain
    Y2 = model1.Xtest
    G2 = model1.G


    print("\nDHA, trace(G) = ", np.trace(G), " G^TG= ", np.trace(np.dot(np.transpose(G),G))/np.shape(G)[0])
    print("DHA, Shared Space Shape: ", np.shape(G))
    print("DHA, Features Shape: ", np.shape(X))
    print("DHA, Loss vec: ", model.ha_loss_vec)
    print("DHA, Error: ", model.ha_loss, ", Runtime: ", model.TrainRuntime)
    error = 0
    for yi in Y:
        error += np.linalg.norm(G - yi) ** 2
    print("DHA, Test Error:", error)


    print("\nGPUHA, Shared Space Shape: ", np.shape(G2))
    print("GPUHA, Feature Shape: ", np.shape(X2))
    print("GPUHA, Error: ", np.mean(model1.Etrain), ", Runtime: ", toc)
    error = 0
    for yi in Y2:
        error += np.linalg.norm(G2 - yi) ** 2
    print("GPUHA, Test Error:", error)
