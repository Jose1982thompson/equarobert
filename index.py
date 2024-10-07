import flet
from flet import *

class ModernNavBar(UserControl):
    def __init__(self, on_select_option, user_name, selected_image=None):
        super().__init__()
        self.on_select_option = on_select_option
        self.user_name = user_name
        self.selected_image = selected_image

    def UserData(self, initials: str, name: str, description: str):
        return Container(
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Container(
                                width=84,
                                height=84,
                                bgcolor="white",
                                alignment=alignment.center,
                                border_radius=84,
                                content=Image(
                                    src=self.selected_image if self.selected_image else "",
                                    fit="cover",
                                    width=84,
                                    height=84,
                                ) if self.selected_image else Text(
                                    value=initials,
                                    size=30,
                                    weight="bold",
                                ),
                            ),
                            Column(
                                spacing=1,
                                alignment="start",
                                controls=[
                                    Text(
                                        value=name,
                                        size=15,
                                        weight='bold',
                                        color="blue",
                                    ),
                                    Text(
                                        value=description,
                                        size=9,
                                        weight='w400',
                                        color="white70",
                                        opacity=1,
                                        animate_opacity=200,
                                    ),
                                ],
                            ),
                        ]
                    )
                ]
            )
        )

    def ContainedIcon(self, icon_name: str, text: str, option: int):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            padding=padding.all(10),
            on_click=lambda e: self.on_select_option(option),
            content=Row(
                controls=[
                    Icon(name=icon_name, size=30),
                    Text(value=text, size=16, weight="bold"),
                ]
            ),
        )

    def build(self):
        return Container(
            width=200,
            height=580,
            alignment=alignment.center,
            content=Column(
                controls=[
                    self.UserData("RL", self.user_name, "Seja Bem-vindo!"),
                    Divider(height=5, color="transparent"),
                    self.ContainedIcon("home", "Home", 1),
                    self.ContainedIcon("menu", "Menu", 2),
                    self.ContainedIcon("settings", "Settings", 3),
                    self.ContainedIcon("info", "Info", 4),
                    self.ContainedIcon("exit_to_app", "Sair", 5),
                ]
            ),
        )

def main(page: Page):
    page.title = "Tutor Inteligente"
    page.bgcolor = "black"

    # Centralizar o conteúdo na página
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # Variável global de imagem selecionada
    selected_image = None

    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Preencha o seu nome"
            page.update()
            return
        if not entrada_senha.value:
            entrada_senha.error_text = "Campo de senha obrigatório"
            page.update()
            return

        nome = entrada_nome.value
        senha = entrada_senha.value
        print(f"Nome: {nome}\nSenha: {senha}")

        page.clean()
        menu_lateral(nome)

    def menu_lateral(nome):
        def opcao_selecionada(opcao):
            if opcao == 1:
                exibir_home(nome)
            elif opcao == 2:
                exibir_menu_exercicio(nome)
            elif opcao == 3:
                exibir_settings(nome)
            elif opcao == 4:
                exibir_info(nome)
            elif opcao == 5:
                page.clean()
                page.add(Text("Saindo do programa.", size=30))
            page.update()

        # Adicionar o menu lateral e a página Home diretamente após o login
        page.add(
            Row(
                controls=[
                    ModernNavBar(opcao_selecionada, nome, selected_image),  # Menu lateral
                    Container(
                        alignment=alignment.center,
                        expand=True,
                        content=Column(
                            controls=[
                                Text(f"Olá, {nome}!\nSeja bem-vindo ao Tutor Inteligente", size=30, color="white"),
                                Text("O Tutor Inteligente é uma ferramenta interativa para ajudar no aprendizado.", size=20, color="white"),
                            ],
                            alignment="center",
                            horizontal_alignment="center"
                        )
                    )
                ]
            )
        )
        page.update()

    def exibir_home(nome):
        page.clean()
        menu_lateral(nome)
        page.update()

    def exibir_menu_exercicio(nome):
        # Título e instruções do exercício
        exercise_title = Text(value="Calcule as raízes da equação x² - 5x + 6", size=20, color='white')
        instructions = Text(value="\nDetermine os coeficientes 'a', 'b' e 'c' da equação:", size=16, color='white')

        # Campos de entrada
        coef_a = TextField(label="Coeficiente 'a'", width=200)
        coef_b = TextField(label="Coeficiente 'b'", width=200)
        coef_c = TextField(label="Coeficiente 'c'", width=200)
        delta_input = TextField(label="Valor do discriminante (Δ)", width=200)
        x1_input = TextField(label="Valor de x1", width=200)
        x2_input = TextField(label="Valor de x2", width=200)

        feedback = Text(value="", size=16, color='red')

        # Respostas corretas
        correct_a = "1"
        correct_b = "-5"
        correct_c = "6"
        correct_delta = "1"
        correct_x1 = "3"
        correct_x2 = "2"

        # Função para verificar se os valores são numéricos
        def is_numeric(value):
            try:
                float(value)  # Tenta converter para float
                return True
            except ValueError:
                return False

        # Função para verificar as respostas
        def check_answers(e):
            if not is_numeric(coef_a.value) or not is_numeric(coef_b.value) or not is_numeric(coef_c.value):
                feedback.value = "Por favor, insira apenas números nos coeficientes."
            elif not is_numeric(delta_input.value) or not is_numeric(x1_input.value) or not is_numeric(x2_input.value):
                feedback.value = "Por favor, insira apenas números no discriminante e nas raízes."
            elif coef_a.value != correct_a:
                feedback.value = "Coeficiente 'a' incorreto. Tente novamente."
            elif coef_b.value != correct_b:
                feedback.value = "Coeficiente 'b' incorreto. Tente novamente."
            elif coef_c.value != correct_c:
                feedback.value = "Coeficiente 'c' incorreto. Tente novamente."
            elif delta_input.value != correct_delta:
                feedback.value = "Valor do discriminante (Δ) incorreto. Tente novamente."
            elif (x1_input.value != correct_x1 and x1_input.value != correct_x2) or (x2_input.value != correct_x2 and x2_input.value != correct_x1):
                feedback.value = "Valores de x1 ou x2 incorretos. Tente novamente."
            else:
                feedback.value = "Você acertou as raízes."

            page.update()

        page.clean()
        page.add(
            Column(
                alignment="center",
                horizontal_alignment="center",
                controls=[
                    exercise_title,
                    instructions,
                    coef_a,
                    coef_b,
                    coef_c,
                    delta_input,
                    x1_input,
                    x2_input,
                    ElevatedButton("Verificar Respostas", on_click=check_answers),
                    feedback,
                    ElevatedButton("Voltar", on_click=lambda e: exibir_home(nome))
                ]
            )
        )
        page.update()

    def exibir_info(nome):
        page.clean()
        page.add(
            Column(
                alignment="center",
                horizontal_alignment="center",
                controls=[
                    Text(f"Informações do sistema, {nome}", size=30, color="white"),
                    ElevatedButton("Voltar", on_click=lambda e: exibir_home(nome)),
                ]
            )
        )
        page.update()

    def exibir_settings(nome):
        nonlocal selected_image  # Permite modificar a variável global

        def atualizar_imagem(src):
            selected_image = src
            exibir_home(nome)  # Voltar para a tela principal com o avatar atualizado

        def mudar_cor_de_fundo(cor):
            page.bgcolor = cor
            exibir_home(nome)

        def criar_seletor_cor(cor):
            return Container(
                width=50,
                height=50,
                bgcolor=cor,
                border_radius=25,
                on_click=lambda e: mudar_cor_de_fundo(cor),
            )

        page.clean()
        page.add(
            Column(
                alignment="center",
                horizontal_alignment="center",
                controls=[
                    Text("Configurações", size=30, color="white"),
                    Row(
                        controls=[
                            criar_seletor_cor("blue"),
                            criar_seletor_cor("green"),
                            criar_seletor_cor("red"),
                        ],
                        alignment="center",
                    ),
                    Text("Escolha uma imagem de perfil:", size=20, color="white"),
                    Row(
                        controls=[
                            Image(src="https://via.placeholder.com/50", on_click=lambda e: atualizar_imagem("https://via.placeholder.com/50")),
                            Image(src="https://via.placeholder.com/50", on_click=lambda e: atualizar_imagem("https://via.placeholder.com/50")),
                        ],
                        alignment="center",
                    ),
                    ElevatedButton("Voltar", on_click=lambda e: exibir_home(nome)),
                ]
            )
        )
        page.update()

    entrada_nome = TextField(label="Nome", width=200)
    entrada_senha = TextField(label="Senha", password=True, width=200)

    page.add(
        Column(
            alignment="center",
            horizontal_alignment="center",
            controls=[
                Text("Login", size=30, color="white"),
                entrada_nome,
                entrada_senha,
                ElevatedButton("Entrar", on_click=login),
            ],
        )
    )

flet.app(target=main)
