from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList()

def exercise_1():
    print("Exercise 1: Build Your Playlist")
    # Append 3 songs
    dll.append("Song: Renai Circulation")
    dll.append("Song: Suzume no Nazo wo Taku ni wa")
    dll.append("Song: Silhouette")
    # Prepend 1 song
    dll.prepend("Song: Baby You")
    dll.print_forward()

def exercise_2():
    print("\nExercise 2: Reverse the Playlist")
    dll.print_backward()

def exercise_3():
    print("\nExercise 3: Insert an Ad in the Middle")
    
    dll.insert_at_position(2, "Ad: BUY PREMIUM SUBSCRIPTION AND I WILL STOP ANNOYING YOU")
    dll.print_forward()

def exercise_4():
    print("\nExercise 4: Remove a Song")
    dll.delete("Song: Silhouette")
    dll.print_forward()

def exercise_5():
    print("\nExercise 5: Search and Replace")
    dll.replace("Song: Renai Circulation", "Song: Renai Circulation (Remix)")
    dll.print_forward()

if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
