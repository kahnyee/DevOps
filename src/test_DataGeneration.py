import DataGeneration

csvfile = "test_Alldatas.csv"
def test_ReadLine():
    #line 5
    result = DataGeneration.ReadLine(csvfile,5)
    answer = [1718220952245.048,37.6,50.5,0.0,8.0,43.0]
    assert (answer == result)

    #line 8
    result2 = DataGeneration.ReadLine(csvfile,8)
    answer2 = [1718220967247.907,37.4,94.9,1.0,5.0,116.0]
    assert (answer2 == result2)

    # line 13
    result3 = DataGeneration.ReadLine(csvfile, 13)
    answer3 = [1718220992251.6055,39.5,82.9,0.0,7.0,336.0]
    assert (answer3 == result3)