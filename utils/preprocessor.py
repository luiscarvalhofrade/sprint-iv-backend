from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class PreProcessor:

    def pre_processor(self, dataset, percentual_test, seed=7):
        """ Cuida de todo o pré-processamento. """
        # divisão em treino e teste
        X_train, X_test, Y_train, Y_test = self.__prepar_holdout(dataset,
                                                                  percentual_test,
                                                                  seed)
        # usando StandardScaler()
        scaler_train = StandardScaler().fit(X_train) # ajuste do scaler com o conjunto de treino
        escaledX_train = scaler_train.transform(X_train)
        scaler_test = StandardScaler().fit(X_test) # ajuste do scaler com o conjunto de treino
        escaledX_test = scaler_test.transform(X_test)
        
        return (escaledX_train, escaledX_test, Y_train, Y_test)
    
    def __prepar_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        data = dataset.values
        X = data[:, 0:-1]
        Y = data[:, -1]
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)