# diary_project.py

class DiaryNode:
    def __init__(self, id, date, title, entry, next_id):
        self.id = id
        self.date = date
        self.title = title
        self.entry = entry
        self.next_id = next_id
        self.next = None  # For linked list pointer

    def __str__(self):
        return f"{self.date} - {self.title}\n{self.entry}\n"


class DiaryLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def print_diary(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def search(self, keyword):
        results = []
        current = self.head
        while current:
            if keyword.lower() in current.title.lower() or keyword.lower() in current.entry.lower():
                results.append(current)
            current = current.next
        return results

    def insert_after_date(self, date, new_node):
        current = self.head
        while current:
            if current.date == date:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Date not found in diary.")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            current = self.head
            while current:
                f.write(f"{current}\n")
                current = current.next


def parse_diary_file(filepath):
    diary_pages = {}
    with open(filepath, "r") as f:
        content = f.read().strip().split('---')
        for entry_text in content:
            lines = entry_text.strip().split("\n")
            if len(lines) < 5:
                continue
            id = int(lines[0].split(": ")[1])
            date = lines[1].split(": ")[1]
            title = lines[2].split(": ")[1]
            entry = lines[3].split(": ")[1]
            next_id_str = lines[4].split(": ")[1]
            next_id = int(next_id_str) if next_id_str != "NULL" else None
            node = DiaryNode(id, date, title, entry, next_id)
            diary_pages[id] = node
    return diary_pages


def build_linked_list(diary_pages):
    # Build linked list from parsed dictionary
    id_to_node = diary_pages
    visited = set()

    # Find starting node (entry that is not pointed to by anyone)
    pointed_to = set(node.next_id for node in id_to_node.values() if node.next_id is not None)
    starting_nodes = [node for node_id, node in id_to_node.items() if node_id not in pointed_to]

    if not starting_nodes:
        print("No unique starting node found.")
        return None

    head = starting_nodes[0]
    current = head
    visited.add(current.id)

    while current and current.next_id is not None:
        next_node = id_to_node.get(current.next_id)
        if not next_node or next_node.id in visited:
            break
        current.next = next_node
        visited.add(next_node.id)
        current = next_node

    diary = DiaryLinkedList()
    diary.head = head
    return diary


if __name__ == "__main__":
    diary_pages = parse_diary_file("diary_pages.txt")
    diary = build_linked_list(diary_pages)
    if diary:
        diary.print_diary()

        keyword = input("\nSearch keyword: ")
        results = diary.search(keyword)
        print(f"\nSearch results for '{keyword}':")
        for result in results:
            print(result)
