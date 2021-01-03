import os

tasks = [
    "Напряженность Н0 магнитного поля в вакууме равна 79,6 нА/м. Опре-делить магнитную индукцию В0 этого поля.",

    "По контуру в виде квадрата со стороной а = 20 см идет ток I = 50 A. Определить магнитную индукцию В в точке "
    "пересечения диагоналей квадрата.",

    "В однородном магнитном поле перпендикулярно линиям магнитной ин-дукции В = 1 Тл расположен прямой провод, "
    "по которому течет ток I = 1 кА. С какой силой F действует поле на отрезок провода длиной l = 1 м?",

    "Найти магнитный поток Ф, создаваемый соленоидом сечения S = 10 см2, если он имеет n = 10 витков на каждый "
    "сантиметр его длины при силе тока I = 20 А.",

    "Во сколько раз изменилась объемная плотность энергии w магнитного поля тороида со стальным сердечником при "
    "изменении магнитной индукции В от 0,5 Тл до 1 Тл и напряженности Н магнитного поля от 220 А/м до 700 А/м, "
    "соответственно.",

    "Висмутовый шарик радиусом R = 1 см помещен в однородное магнит-ное поле В = 0,5 Тл. Определить "
    "магнитный момент pm, приобретенный ша-риком, если магнитная восприимчивость $ \\chi $ висмута "
    "равна $ –1,5 * 10^{–4}."
]

t = False

if __name__ == '__main__':
    num_of_tasks = len(tasks)

    for i in range(num_of_tasks):
        with open("C:\\Users\\kiril\\Universety\\2_COURSE\\1_SEM\\PHISICS\\Tasks\\task3\\IHW3_Leskin_9892\\modules"
                  "\\chapters\\task_"+str(i+1)+".tex", "w", encoding='utf-8') as f:
            print(f"\\input{{modules/chapters/task_{i + 1}.tex}}\n\n\\newpage\n")
            task_num = i + 1 if i != 1 else i
            t = 1 if i != 1 else 9

            s = f"""
\\begin{{center}}
    \\textbf{{Задача 3.{task_num} --- {t}}}
\\end{{center}}

\\underline{{\\textbf{{Условие:}}}}

{tasks[i]}

\\underline{{\\textbf{{Решение:}}}}

0

\\underline{{\\textbf{{Ответ:}}}}

0
"""
            f.write(s)

