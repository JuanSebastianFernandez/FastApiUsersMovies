import asyncio


# def reloj():
#     for seg in range(1,6):
#         print(seg)
#         time.sleep(1)

async def funcion_lenta():
    print("Inicio de la funcion lenta")
    await asyncio.sleep(5)
    print("Fin de la funcion lenta")


async def main():
    print("Inicio del programa")
    await funcion_lenta()
    print("Fin del programa")

async def main2():
    print("otro")
if __name__ == "__main__": 
    asyncio.run(main())
    asyncio.run(main2())