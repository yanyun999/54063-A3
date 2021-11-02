print('-'*30, 'welcome to Fighting Zombies!', '-'*30)

print('please choose your character :')
print('\t 1. Cherry Bomb')
print('\t 2. Sunflower')
player_choice = input('please choose [1-2]:')

print('-'*90)

if player_choice == '1':
    print('you will play as the [Cherry Bomb]!')
elif player_choice == '2':
    print('Sunflower is unable to beat the zombie! The system will automatically assign you as [Cherry Bomb]!')
else:
    print('Error！The system will automatically assign you as [Cherry Bomb]!')

health_point = 2
combat_power = 2
boss_life = 10
boss_combat = 10

print(' ')
print(f'Cheery Bomb, your health point is {health_point} , your combat power is {combat_power}')

while True:
    print(' ')
    print('please choose your next move :')
    print('\t 1. upgrade level')
    print('\t 2. fight the zombie')
    print('\t 3. escape')
    player_choice = input('please choose [1-3] :')

    if player_choice == '1':
        health_point += 2
        combat_power += 2
        print(f'congrats! your health point now is {health_point} and your combat power is {combat_power}!')

    elif player_choice == '2':
        boss_life -= combat_power
        print(' ')
        print('you attacked the zombie!')
        if boss_life <= 0:
            print(f'--victory--! the zombie has taken {combat_power} damage and been defeated! ')
            break
        health_point -= boss_combat
        print('the zombie attacked you!')
        if health_point <= 0:
            print(f'--oh no--! your attack was not enough! the zombie defeated you! GAME OVER')
            break
    elif player_choice == '3':
        print(' ')
        print('you escaped! GAME OVER')
        break


































