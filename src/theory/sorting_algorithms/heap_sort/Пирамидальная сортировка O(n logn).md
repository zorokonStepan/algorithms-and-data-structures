```
      Пирамидальная сортировка подходит для работы с полными бинарными деревьями в массиве.
    В ней используется структура данных, называемая куча.
    
    1. Постройте max-heap из входных данных.
    2. На данном этапе самый большой элемент хранится в корне кучи. 
       Замените его на последний элемент кучи, а затем уменьшите ее размер на 1. 
       Наконец, преобразуйте полученное дерево в max-heap с новым корнем.
    3. Повторяйте вышеуказанные шаги, пока размер кучи больше 1.
```

![](./heap_sort.gif)
