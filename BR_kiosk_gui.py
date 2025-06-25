import tkinter as tk
from tkinter import messagebox

class BRKioskGUI:
    MENU_PRICES = {
        "아이스크림": {1: 3900, 2: 7300, 3: 9800, 4: 18500, 5: 26000, 6: 31500},
        "케이크": 25000,
        "커피": 4500,
        "음료": 4000,
        "디저트": 6000
    }

    def __init__(self, root):
        self.root = root
        self.root.title("베스킨라빈스 키오스크")

        # 상태 값
        self.menu_type = ""
        self.size = 0
        self.place = ""
        self.icecream_list = []
        self.spoon = 0
        self.dryice = 0
        self.order_list = []
        self.total_price = 0
        self.number = 1

        # 시작화면
        self.label = tk.Label(root, text="** 베스킨라빈스에 오신 것을 환영합니다 **")
        self.label.pack(pady=10)

        self.start_btn = tk.Button(root, text="주문 시작", command=self.step_1)
        self.start_btn.pack()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def step_1(self):
        self.clear()
        tk.Label(self.root, text="종류를 선택해 주세요").pack()
        for name in ["아이스크림", "케이크", "커피", "음료", "디저트"]:
            tk.Button(self.root, text=name, command=lambda n=name: self.select_type(n)).pack(pady=2)

    def select_type(self, menu_type):
        self.menu_type = menu_type
        if menu_type == "아이스크림":
            self.step_2()
        elif menu_type == "케이크" or menu_type == "디저트":
            self.step_3()
        else:
            self.step_4()

    def step_2(self):
        self.clear()
        tk.Label(self.root, text="사이즈를 선택해 주세요").pack()
        size_dict = {1: "싱글", 2: "더블", 3: "파인트", 4: "쿼터", 5: "패밀리", 6: "하프갤런"}
        for num, name in size_dict.items():
            tk.Button(self.root, text=f"{name} ({num})", command=lambda n=num: self.select_size(n)).pack(pady=2)

    def select_size(self, size):
        self.size = size
        self.step_3()

    def step_3(self):
        self.clear()
        tk.Label(self.root, text="스푼 개수를 입력해 주세요").pack()
        self.spoon_entry = tk.Entry(self.root)
        self.spoon_entry.pack()
        tk.Button(self.root, text="확인", command=self.get_spoon).pack(pady=5)

    def get_spoon(self):
        try:
            self.spoon += int(self.spoon_entry.get())
            self.step_4()
        except ValueError:
            messagebox.showerror("입력 오류", "숫자를 입력해 주세요.")

    def step_4(self):
        self.clear()
        tk.Label(self.root, text="식사 장소를 선택해 주세요").pack()
        tk.Button(self.root, text="매장", command=lambda: self.select_place("매장")).pack(pady=2)
        tk.Button(self.root, text="포장", command=lambda: self.select_place("포장")).pack(pady=2)

    def select_place(self, place):
        self.place = place
        if self.place == "포장" and self.menu_type in ["아이스크림", "케이크"]:
            self.step_5()
        else:
            self.step_6()

    def step_5(self):
        self.clear()
        tk.Label(self.root, text="이동시간을 입력해 주세요 (분)").pack()
        self.dryice_entry = tk.Entry(self.root)
        self.dryice_entry.pack()
        tk.Button(self.root, text="확인", command=self.get_dryice).pack(pady=5)

    def get_dryice(self):
        try:
            mins = int(self.dryice_entry.get())
            self.dryice += mins // 60
            self.step_6()
        except ValueError:
            messagebox.showerror("입력 오류", "숫자를 입력해 주세요.")

    def step_6(self):
        self.clear()
        if self.menu_type == "아이스크림":
            tk.Label(self.root, text=f"{self.size}가지의 메뉴를 입력해 주세요").pack()
            self.menu_entry = tk.Entry(self.root)
            self.menu_entry.pack()
            tk.Button(self.root, text="추가", command=self.add_icecream_menu).pack(pady=2)
        else:
            tk.Label(self.root, text="메뉴명을 입력해 주세요").pack()
            self.menu_entry = tk.Entry(self.root)
            self.menu_entry.pack()
            tk.Button(self.root, text="확인", command=self.add_other_menu).pack(pady=2)

    def add_icecream_menu(self):
        menu = self.menu_entry.get()
        if menu:
            self.icecream_list.append(menu)
            if len(self.icecream_list) < self.size:
                self.menu_entry.delete(0, tk.END)
            else:
                order = f"{self.menu_type} {self.icecream_list} {self.place}"
                self.order_list.append(order)
                price = self.MENU_PRICES["아이스크림"][self.size]
                self.total_price += price
                messagebox.showinfo("주문", f"{order}\n가격: {price}원")
                self.step_7()

    def add_other_menu(self):
        menu = self.menu_entry.get()
        if menu:
            order = f"[{menu}] {self.menu_type} {self.place}"
            self.order_list.append(order)
            price = self.MENU_PRICES[self.menu_type]
            self.total_price += price
            messagebox.showinfo("주문", f"{order}\n가격: {price}원")
            self.step_7()

    def step_7(self):
        self.clear()
        tk.Label(self.root, text="주문을 계속하시겠습니까?").pack()
        tk.Button(self.root, text="계속", command=self.reset_and_restart).pack(pady=2)
        tk.Button(self.root, text="마치기", command=self.step_8).pack(pady=2)

    def reset_and_restart(self):
        self.icecream_list = []
        self.menu_type = ""
        self.size = 0
        self.step_1()

    def step_8(self):
        self.clear()
        tk.Label(self.root, text="주문 내역:").pack()
        tk.Label(self.root, text=str(self.order_list)).pack()
        tk.Label(self.root, text=f"숟가락: {self.spoon}개, 드라이아이스: {self.dryice}덩이").pack()
        tk.Label(self.root, text=f"총 결제 금액: {self.total_price}원").pack()
        tk.Button(self.root, text="결제하기", command=self.step_9).pack(pady=5)

    def step_9(self):
        self.clear()
        tk.Label(self.root, text=f"결제가 완료되었습니다.\n수령번호: {self.number:03d}\n영수증을 수령하세요.").pack()
        tk.Button(self.root, text="종료", command=self.root.quit).pack(pady=5)

# 실행
root = tk.Tk()
app = BRKioskGUI(root)
root.mainloop()
