import numpy as np
import matplotlib.pyplot as plt

# Временные параметры
dt = 1 # Шаг времени
t_max = 500 # Максимальное время моделирования
num_steps = int(t_max / dt)
time = np.linspace(0, t_max, num_steps)

#введем систему штрафов за разные типы взаиводействия
Hawk_Hawk_loss = -8
#так как ястребы - агрессивные животные, во время встречи два ястреба начнут сражаться,
#и один из них проиграет 
Hawk_Hawk_win = +14
#второй выйграет и получит сколько-то очков, а так же вычтем 10 очков, как затраты на ведение боя.
Hawk_Hawk = Hawk_Hawk_loss*0.5+Hawk_Hawk_win*0.5
#Так как мы считаем, что все ястребы внутри популяции равны друг другу по характеристикам, то вероятность выйгрыша каждой птицы равен 50%


Pigeon_Pigeon = 0 #так как голуби - миролюбивые животные, то во время встречи они совершат акт внутривидового
#взаимодействия,на что оба потратят небольшое количество энергии

#межвидовые взаимодействия
Hawk_Pigeon = +15
#Так как голубь слабее ястреба, во время сражения он получит урон
Pigeon_Hawk = -8
#Так как ястреб сильнее голубя, во время сражения он получит приемущество

#Введем список для ястребов и голубей
Hawk = np.zeros(num_steps)
Pigeon = np.zeros(num_steps)

#начальные данные популяции
Hawk[0] = 500
Pigeon[0] = 500

# Функция для вычисления взаимодействия
def act_of_interaction(Hawk, Pigeon):
    sum = Hawk + Pigeon
    Hawk = Hawk/sum
    Pigeon = Pigeon/sum
    dot_Hawk = Hawk * (Hawk_Hawk - Hawk_Pigeon * Pigeon)
    dot_Pigeon = Pigeon * (Pigeon_Pigeon + Pigeon_Hawk * Hawk)
    return dot_Hawk, dot_Pigeon

#пользуемся формулой
for i in range(int(num_steps)-1):
    dot_Hawk, dot_Pigeon = act_of_interaction(Hawk[i], Pigeon[i])
    
    # Добавляем случайные возмущения
    noise = np.random.normal(0, 0.1)
    
    Hawk[i+1] = Hawk[i] + (dot_Hawk + noise) * dt
    Pigeon[i+1] = Pigeon[i] + (dot_Pigeon + noise) * dt

z = (Pigeon_Pigeon - Hawk_Hawk)/(Hawk_Hawk - Hawk_Pigeon - Pigeon_Hawk + Pigeon_Pigeon)

print(z, 1-z)
# Визуализация результатов

plt.plot(time, Pigeon, label='Численность голубей')
plt.plot(time, Hawk, label='Численность ястребов')
plt.xlabel('Время')
plt.ylabel('Численность')
plt.title('модель взаимодействия')
plt.legend()
plt.grid(True)
plt.show()