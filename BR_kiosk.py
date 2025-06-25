class BRKiosk:
    MENU_PRICES = {
        "아이스크림": {1: 3900, 2: 7300, 3: 9800, 4: 18500, 5: 26000, 6: 31500},
        "케이크": 25000,
        "커피": 4500,
        "음료": 4000,
        "디저트": 6000
    }

    def __init__(self):
        self.menu_type = ""        # 선택한 메뉴 종류 (아이스크림, 케이크 등)
        self.size = 0              # 아이스크림 사이즈 (숫자: 1 ~ 6)  
        self.place = ""            # 매장 / 포장 여부
        self.icecream_list = []    # 아이스크림 맛 리스트
        self.spoon = 0             # 스푼 개수
        self.dryice = 0            # 드라이아이스 덩이 수
        self.order_list = []       # 주문 내역 저장
        self.total_price = 0       # 총 결제 금액
        self.number = 1            # 수령번호 (고정값: 001)

    def safe_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("⚠️ 숫자만 입력해 주세요.")

    def start(self):
        print("** 베스킨라빈스에 오신 것을 환영합니다. **\n")
        self.step_1()

    def step_1(self):
        print("\n종류를 선택해 주세요.\n아이스크림은 1, 케이크는 2, 커피는 3, 음료는 4, 디저트는 5를 입력해 주세요.")
        dic = {1: "아이스크림", 2: "케이크", 3: "커피", 4: "음료", 5: "디저트"}
        answer = self.safe_int_input("입력: ")
        self.menu_type = dic.get(answer, "")
        if not self.menu_type:
            print("⚠️ 올바른 번호를 입력해 주세요.")
            return self.step_1()

        if answer == 1:
            self.step_2()
        elif answer == 2 or answer == 5:
            self.step_3()
        elif answer == 3 or answer == 4:
            self.step_4()

    def step_2(self):
        print("\n사이즈를 선택해 주세요.\n\
            SIZE       |    NUMBER     \n\
        -----------------------------\n\
           싱글레귤러  |      1       \n\
           더블레귤러  |      2       \n\
            파인트     |      3       \n\
             쿼터      |      4        \n\
            패밀리     |      5        \n\
            하프갤런   |      6         \n ")
        self.size = self.safe_int_input("입력: ")
        if self.size not in self.MENU_PRICES["아이스크림"]:
            print("⚠️ 올바른 사이즈를 선택해 주세요.")
            return self.step_2()
        self.step_3()

    def step_3(self):
        print("\n스푼 개수를 입력해 주세요.")
        self.spoon += self.safe_int_input("입력: ")
        self.step_4()

    def step_4(self):
        print("\n식사 장소를 선택해 주세요.\n매장식사는 1번, 포장은 2번을 눌러주세요.")
        dic = {1: "매장", 2: "포장"}
        answer = self.safe_int_input("입력: ")
        self.place = dic.get(answer, "")
        if not self.place:
            print("⚠️ 올바른 번호를 입력해 주세요.")
            return self.step_4()
        self.step_5()

    def step_5(self):
        if self.place == "포장" and (self.menu_type == '아이스크림' or self.menu_type == '케이크'):
            print("\n이동시간을 선택해 주세요.(한 시간에 드라이아이스 1덩이 제공)")
            self.dryice += self.safe_int_input("입력: ")
        self.step_6()

    def step_6(self):
        if self.menu_type == "아이스크림":
            print(f"\n{self.size}가지의 메뉴를 선택해 주세요.")
            while len(self.icecream_list) < self.size:
                menu = input(f"{len(self.icecream_list) + 1}번째 메뉴: ")
                self.icecream_list.append(menu)
            print("\n아이스크림을 모두 선택하셨습니다.")
            order = f"{self.menu_type} {self.icecream_list} {self.place}"
            self.order_list.append(order)
            price = self.MENU_PRICES["아이스크림"][self.size]
        else:
            menu = input("\n메뉴를 선택해 주세요: ")
            order = f"[{menu}] {self.menu_type} {self.place}"
            self.order_list.append(order)
            price = self.MENU_PRICES[self.menu_type]

        print(f"선택하신 내용은 {order}이며, 가격은 {price}원 입니다.")
        self.total_price += price
        self.step_7()

    def step_7(self):
        print("\n\n주문을 계속하시려면 1을, 주문을 마치시려면 2를 눌러주세요.")
        answer = self.safe_int_input("입력: ")
        if answer == 1:
            self.reset_single_order()
            self.step_1()
        elif answer == 2:
            self.show_summary()
            self.step_8()
        else:
            print("⚠️ 올바른 번호를 입력해 주세요.")
            self.step_7()

    def reset_single_order(self):
        self.icecream_list = []

    def show_summary(self):
        print("\n\n---------------------------------------------------------")
        print("\n주문하신 내용은 다음과 같습니다:\n")
        print(self.order_list)
        print(f"숟가락은 {self.spoon}개, 드라이아이스는 {self.dryice}덩이 제공될 것입니다.")

    def step_8(self):
        print(f"결제 금액은 {self.total_price}원입니다.\n카드 투입구에 카드를 넣어주세요.")
        self.step_9()

    def step_9(self):
        print(f"\n\n결제가 완료되었습니다.\n수령번호는 {self.number:03d}입니다.\n영수증을 수령하세요.")
        self.step_10()

    def step_10(self):
        print("\n\n** 오늘도 저희 베스킨라빈스를 이용해주셔서 감사합니다. **\n** 안녕히 가세요. **")

# 프로그램 실행
kiosk = BRKiosk()
kiosk.start()
