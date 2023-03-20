from django.shortcuts import render



# from .forms import CategoriesForm



from django.db import connection



def jls_extract_def2():

    return  '''  select avg(speed),maker

                from (  select speed, maker

                        from laptop,product

                        where product.model=laptop.model) p

                        group by maker
            '''


def jls_extract_def4():
    return '''SELECT model, price
                        FROM (select printer.model, maker, price
                            from printer, product
                            where printer.model=product.model) p
                        WHERE price IN (
                            SELECT MAX(price)
                            FROM (select printer.model, maker, price
                            from printer, product
                            where printer.model=product.model) p
                            GROUP BY maker
                        );'''


def userInputSQL(request):



    if request.method == "POST":
        


        if request.POST.get('userInputSQL'):   
            


            cursor=connection.cursor()    


            cursor.execute(request.POST.get('userInputSQL'))
            cursor.close()



        if request.POST.get('readTable'): 
            


            table=request.POST.get('readTable')   


            cursor=connection.cursor()  


            sql = "SELECT * FROM "+ table


            try: 


                cursor.execute(sql)


                results=cursor.fetchall()


                return render(request, "myApp/hw.html",{'result1':results})


            except :
                cursor.close()



        if request.POST.get('q1'):


            cursor=connection.cursor()  


            sql = "select avg(hd) from PC"


            try: 


                cursor.execute(sql)


                results=cursor.fetchall()


                return render(request, "myApp/hw.html",{'result2':results})


            except :
                cursor.close()
        


        if request.POST.get('q2'):


            cursor=connection.cursor()  


            sql = jls_extract_def2()



            try: 


                cursor.execute(sql)


                results=cursor.fetchall()


                return render(request, "myApp/hw.html",{'result2':results})


            except :
                cursor.close()
        


        if request.POST.get('q3'):


            cursor=connection.cursor()  


            sql1 = '''   select price,maker

                        from (select price,laptop.model, maker

                        from laptop,product

                        where product.model=laptop.model) p

                        group by maker

                        having count(model)=1   '''


            try: 

                sql2="SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));"

                cursor.execute(sql2)
                cursor.execute(sql1)

                results=cursor.fetchall()
                print(results)

                return render(request, "myApp/hw.html",{'result2':results})


            except :
                cursor.close()
        


        if request.POST.get('q4'):


            cursor=connection.cursor()  


            sql = jls_extract_def4()


            try: 


                cursor.execute(sql)


                results=cursor.fetchall()


                return render(request, "myApp/hw.html",{'result2':results})


            except :
                cursor.close()


    return render(request, "myApp/hw.html")
        
    




# def readTable(request):



#     if request.method == "POST":


#         print(2)


#         if request.POST.get('readTable'):


#             print(21)


#             cursor=connection.cursor()



#             sql = "SELECT * FROM laptop"


#             cursor.execute(sql)



#             result=cursor.fetchall()


#             print (result)
            


#     return render(request, "myApp/hw.html", {'result' : result})

  