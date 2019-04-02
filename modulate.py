import numpy as np

def encode2d(x):
    #x= np.random.randint(0, 2, [1, 64]).astype('float32')
    length_x=x.size/2
  #  data=np.arange(length_x)
    data_odd=x[:,0::2]
    data_even=x[:,1::2]
    qpsk_data=[]
    for ii in range(int(length_x)):
        if (data_odd[:,ii]== 0. and data_even[:,ii]==0.):
            qpsk_data.append( [-np.sqrt(2)/2,-np.sqrt(2)/2] )
        elif data_odd[:,ii]==0 and data_even[:,ii]==1:
            qpsk_data.append( [-np.sqrt(2) / 2 , np.sqrt(2) / 2] )
        elif data_odd[:,ii]==1 and data_even[:,ii]==0:
            qpsk_data.append( [np.sqrt(2) / 2 , -np.sqrt(2) / 2] )
        elif data_odd[:,ii] == 1 and data_even[:,ii] == 1:
            qpsk_data.append( [np.sqrt(2) / 2 , np.sqrt(2) / 2] )

    return np.array(qpsk_data)




