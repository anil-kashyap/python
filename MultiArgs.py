def test_var_args(*normal,**argv):
    print("First normal arg:", normal)
    for anil in argv:
        print ("another arg through *argv :",anil)

test_var_args('yasoob','python','eggs','test')