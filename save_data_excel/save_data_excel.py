import pandas as pd

def main():
    t1=[0, 10, 20, 30, 40, 50, 60]
    d1=[10, 20, 30, 20, 15, 30, 45]

    t2=[70, 80, 90, 100, 110, 120, 130]
    d2=[15, 25, 35, 25, 20, 35, 50]
    
    mydataframe1 = pd.DataFrame({
                    'time': t1,
                    'Data': d1
                   })
    mydataframe2 = pd.DataFrame({
                    'time': t2,
                    'Data': d2
                   })

    writer = pd.ExcelWriter('myexcel.xlsx', engine='xlsxwriter')

    mydataframe1.to_excel(writer, sheet_name='Sheet1')
    mydataframe2.to_excel(writer, sheet_name='Sheet2')

    writer.save()

if __name__ == "__main__" : main()
