import os
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
                exibir_menu_principal(nome)  # Corrigido para chamar a função correta
            elif opcao == 3:
                exibir_settings(nome)
            elif opcao == 4:
                exibir_info(nome)  # Corrigido para chamar a função correta
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
        menu_lateral(nome)  # Certifique-se de que o menu lateral é exibido corretamente
        page.update()

    def exibir_menu_principal(nome):
        # Função de exibição do menu principal (substitua com o conteúdo desejado)
        page.clean()
        page.add(
            Column(
                alignment="center",
                horizontal_alignment="center",
                controls=[
                    Text(f"Bem-vindo ao Menu, {nome}", size=30, color="white"),
                    ElevatedButton("Voltar", on_click=lambda e: exibir_home(nome)),
                ]
            )
        )
        page.update()

    def exibir_info(nome):
        # Função de exibição da página "Info"
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
        def atualizar_imagem(src):
            nonlocal selected_image
            selected_image = src
            exibir_home(nome)  # Voltar para a tela principal com o avatar atualizado

        def mudar_cor_de_fundo(cor):
            page.bgcolor = cor
            exibir_home(nome)

        # Funções auxiliares para os botões de seleção
        def criar_seletor_cor(cor):
            return Container(
                width=50,
                height=50,
                bgcolor=cor,
                border_radius=25,
                on_click=lambda e: mudar_cor_de_fundo(cor)
            )

        page.clean()
        page.add(
            Column(
                controls=[
                    Text("Escolha uma imagem de perfil", size=20, color="white"),
                    Row(
                        controls=[
                            ElevatedButton("Avatar 1", on_click=lambda e: atualizar_imagem("imagens/perfil1.png")),
                            ElevatedButton("Avatar 2", on_click=lambda e: atualizar_imagem("imagens/perfil2.png")),
                        ]
                    ),
                    Text("Escolha uma cor de fundo", size=20, color="white"),
                    Row(
                        controls=[
                            criar_seletor_cor("black"),
                            criar_seletor_cor("white"),
                            criar_seletor_cor("green"),
                            criar_seletor_cor("blue"),
                            criar_seletor_cor("red"),
                        ]
                    ),
                    ElevatedButton("Voltar", on_click=lambda e: exibir_home(nome)),
                ],
                alignment="center",
                horizontal_alignment="center",
            )
        )
        page.update()

    entrada_nome = TextField(label="Nome", width=300)
    entrada_senha = TextField(label="Senha", password=True, width=300)

    page.add(
        Column(
            alignment="center",
            horizontal_alignment="center",
            controls=[
                Text("Login", size=40, color="white"),
                entrada_nome,
                entrada_senha,
                ElevatedButton("Entrar", on_click=login),
            ],
        )
    )

flet.app(target=main)
