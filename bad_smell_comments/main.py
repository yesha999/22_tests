# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def move(self, field, x_coord, y_coord, direction, is_fly=False, is_crawl=False, speed = 1):
        """Функция реализует перемещение юнита по полю.
        """
        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly: 
            speed *= 1.2 
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + speed
        if is_crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + speed

        field.set_unit(x=new_x, y=new_y, unit=self)


    
    
