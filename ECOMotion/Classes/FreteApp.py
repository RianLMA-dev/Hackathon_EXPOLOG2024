import tkinter as tk
from tkinter import ttk
from constantes import *

class FreteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Fretes")
        self.root.geometry("1200x750")

        # Dados dos fretes (adicionando o frete inicial)
        self.fretes = [{
            "origem": "Juazeiro-do-Norte",
            "destino": "Russas",
            "distancia": 364.8,
            "modelo": "Volkswagen Delivery 11.180",
            "capacidade": 7400,  # Capacidade do caminhão
            "tipo": "Mobilia",
            "rendimento": 5.4,  # Rendimento inicial
            "valor": (364.8/5.4)*gas,
            "emissao": (364.8/5.4)*emissao_disel,
            "cargas": [],  # Lista de cargas
            
        }]

        # Frames para cada tela
        self.tela_inicio = tk.Frame(root, bg="#1E5128")
        self.tela_criar_frete = tk.Frame(root, bg="#1E5128")
        self.tela_menu = tk.Frame(root, bg="#1E5128")
        self.tela_cargas = tk.Frame(root, bg="#1E5128")  # Tela para gerenciar cargas
        self.tela_dados = tk.Frame(root, bg="#1E5128")

        # Inicializa as telas
        self.configurar_tela_inicio()
        self.configurar_tela_criar_frete()
        self.configurar_tela_menu()
        self.configurar_tela_cargas()
        #self.configurar_tela_dados()

        # Mostra a tela inicial
        self.mostrar_tela(self.tela_inicio)

    def mostrar_tela(self, tela):
        """Alterna entre as telas."""
        self.tela_inicio.pack_forget()
        self.tela_criar_frete.pack_forget()
        self.tela_menu.pack_forget()
        self.tela_cargas.pack_forget()
        self.tela_dados.pack_forget()

        tela.pack(fill="both", expand=True)

        # Atualiza tabela de fretes ao voltar para o menu
        if tela == self.tela_menu:
            self.atualizar_lista_fretes()

    def configurar_tela_inicio(self):
        """Configura a tela inicial."""
        tk.Label(
            self.tela_inicio, text="Bem-vindo à ECOMotion", bg="#1E5128",
            fg="white", font=("Nexa Heavy", 26)
        ).pack(pady=20)

        tk.Button(
            self.tela_inicio, text="Criar Frete", command=lambda: self.mostrar_tela(self.tela_criar_frete),
            width=20, height=2
        ).pack(pady=10)

        tk.Button(
            self.tela_inicio, text="Ver Fretes", command=lambda: self.mostrar_tela(self.tela_menu),
            width=20, height=2
        ).pack(pady=10)

        
    def configurar_tela_criar_frete(self):
        """Configura a tela de criação de frete."""
        tk.Label(
            self.tela_criar_frete, text="Criar Novo Frete", bg="#1E5128",
            fg="white", font=("Nexa Heavy", 26)
        ).pack(pady=20)

        # Alterar a cor de fundo do frame
        self.frame_inputs = tk.Frame(self.tela_criar_frete, padx=10, pady=10, bg="#1E5128")
        self.frame_inputs.pack(padx=20, pady=20)

        # Primeira linha
        tk.Label(self.frame_inputs, text="Origem", bg="#1E5128", fg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.origem_entry = ttk.Entry(self.frame_inputs, width=20)
        self.origem_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Destino", bg="#1E5128", fg="white").grid(row=0, column=2, sticky="w", padx=10, pady=5)
        self.destino_entry = ttk.Entry(self.frame_inputs, width=20)
        self.destino_entry.grid(row=0, column=3, padx=5, pady=5)

        # Segunda linha
        tk.Label(self.frame_inputs, text="Distância (km)", bg="#1E5128", fg="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.distancia_entry = ttk.Entry(self.frame_inputs, width=20)
        self.distancia_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Veículo (modelo)", bg="#1E5128", fg="white").grid(row=1, column=2, sticky="w", padx=10, pady=5)
        self.modelo_entry = ttk.Entry(self.frame_inputs, width=20)
        self.modelo_entry.grid(row=1, column=3, padx=5, pady=5)

        # Terceira linha
        tk.Label(self.frame_inputs, text="Capacidade (kg)", bg="#1E5128", fg="white").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.capacidade_entry = ttk.Entry(self.frame_inputs, width=20)
        self.capacidade_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Tipo de Frete", bg="#1E5128", fg="white").grid(row=2, column=2, sticky="w", padx=10, pady=5)
        self.tipo_entry = ttk.Entry(self.frame_inputs, width=20)
        self.tipo_entry.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Tipo de Frete", bg="#1E5128", fg="white").grid(row=2, column=2, sticky="w", padx=10, pady=5)
        self.tipo_entry = ttk.Entry(self.frame_inputs, width=20)
        self.tipo_entry.grid(row=2, column=3, padx=5, pady=5)

        # Nova linha para o rendimento
        tk.Label(self.frame_inputs, text="Rendimento (km/l)", bg="#1E5128", fg="white").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.rendimento_entry = ttk.Entry(self.frame_inputs, width=20)
        self.rendimento_entry.grid(row=3, column=1, padx=5, pady=5)


        # Botão para salvar o frete
        tk.Button(
            self.tela_criar_frete, text="Salvar Frete", command=self.salvar_frete,
            width=20, height=2
        ).pack(pady=10)

        # Botão para voltar ao menu
        tk.Button(
            self.tela_criar_frete, text="Voltar", command=lambda: self.mostrar_tela(self.tela_menu),
            width=20, height=2
        ).pack(pady=10)

    def salvar_frete(self):
        """Salva o frete e retorna ao menu."""
        try:
            origem = self.origem_entry.get()
            destino = self.destino_entry.get()
            distancia = float(self.distancia_entry.get())
            modelo = self.modelo_entry.get()
            capacidade = float(self.capacidade_entry.get())
            tipo = self.tipo_entry.get()
            rendimento = float(self.rendimento_entry.get())

            novo_frete = {
                "origem": origem,
                "destino": destino,
                "distancia": distancia,
                "modelo": modelo,
                "capacidade": capacidade,
                "tipo": tipo,
                "rendimento": rendimento,
                "valor": (distancia/rendimento) * gas, 
                "emissao": (distancia/rendimento) * emissao_disel,
                "cargas": []  # Lista de cargas vazia
            }

            self.fretes.append(novo_frete)

            # Limpa os campos
            self.origem_entry.delete(0, tk.END)
            self.destino_entry.delete(0, tk.END)
            self.distancia_entry.delete(0, tk.END)
            self.modelo_entry.delete(0, tk.END)
            self.capacidade_entry.delete(0, tk.END)
            self.tipo_entry.delete(0, tk.END)
            self.rendimento_entry.delete(0, tk.END)

            # Retorna ao menu
            self.mostrar_tela(self.tela_menu)

        except ValueError:
            print("Erro: Verifique os valores inseridos.")

    def configurar_tela_menu(self):
        """Configura a tela do menu."""
        tk.Label(
            self.tela_menu, text="Lista de Fretes", bg="#1E5128",
            fg="white", font=("Arial", 16)
        ).pack(pady=20)

        # Botão para criar novo frete
        tk.Button(
            self.tela_menu, text="Criar Novo Frete", command=lambda: self.mostrar_tela(self.tela_criar_frete),
            width=20, height=2
        ).pack(pady=10)

        # Tabela de Fretes
        self.tabela_fretes = ttk.Treeview(self.tela_menu, columns=(
            "Origem", "Destino", "Distância", "Modelo", "Capacidade", "Tipo", "Rendimento (km/l)", "Valor", "Emissao"), show="headings")
        self.tabela_fretes.pack(fill="both", expand=True)

        # Definir as colunas
        self.tabela_fretes.heading("Origem", text="Origem")
        self.tabela_fretes.heading("Destino", text="Destino")
        self.tabela_fretes.heading("Distância", text="Distância (km)")
        self.tabela_fretes.heading("Modelo", text="Modelo")
        self.tabela_fretes.heading("Capacidade", text="Capacidade (kg)")
        self.tabela_fretes.heading("Tipo", text="Tipo")
        self.tabela_fretes.heading("Rendimento (km/l)", text="Rendimento (km/l)")
        self.tabela_fretes.heading("Valor", text="Valor (R$)")
        self.tabela_fretes.heading("Emissao", text="Emissão (Kg/L)")

        # Define as larguras das colunas
        self.tabela_fretes.column("Origem", width=120, anchor="center", stretch=tk.YES)
        self.tabela_fretes.column("Destino", width=120, anchor="center", stretch=tk.YES)
        self.tabela_fretes.column("Distância", width=150, anchor="center", stretch=tk.YES)
        self.tabela_fretes.column("Modelo", width=200, anchor="center", stretch=tk.YES)
        self.tabela_fretes.column("Capacidade", width=150, anchor="center", stretch=tk.YES)
        self.tabela_fretes.column("Tipo", width=120, anchor="center", stretch=tk.YES)
        self.tabela_fretes.column("Rendimento (km/l)", width=150, anchor="center", stretch=tk.YES)
        self.tabela_fretes.column("Valor", width=150, anchor="center", stretch=tk.YES)
        self.tabela_fretes.column("Emissao", width=150, anchor="center", stretch=tk.YES)

        # Botão para gerenciar as cargas
        tk.Button(
            self.tela_menu, text="Gerenciar Cargas", command=self.gerenciar_cargas,
            width=20, height=2
        ).pack(pady=10)

    def gerenciar_cargas(self):
        """Gerencia as cargas do frete selecionado."""
        # Obtém o frete selecionado
        selecionado = self.tabela_fretes.selection()
        if selecionado:
            frete_idx = self.tabela_fretes.index(selecionado[0])
            self.frete_selecionado = self.fretes[frete_idx]
            self.mostrar_tela(self.tela_cargas)

    def configurar_tela_cargas(self):
        """Configura a tela de cargas."""
        tk.Label(
            self.tela_cargas, text="Gerenciar Cargas", bg="#1E5128",
            fg="white", font=("Arial", 16)
        ).pack(pady=20)

        # Frame para entrada de carga
        self.frame_carga = tk.Frame(self.tela_cargas, padx=10, pady=10, bg="#1E5128")
        self.frame_carga.pack(padx=20, pady=20)

        # Entradas para carga
        tk.Label(self.frame_carga, text="Empresa", bg="#1E5128", fg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.empresa_entry = ttk.Entry(self.frame_carga, width=20)
        self.empresa_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_carga, text="Peso (kg)", bg="#1E5128", fg="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.peso_entry = ttk.Entry(self.frame_carga, width=20)
        self.peso_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botão para adicionar carga
        tk.Button(
            self.tela_cargas, text="Adicionar Carga", command=self.adicionar_carga,
            width=20, height=2
        ).pack(pady=10)

        # Botão para voltar ao menu
        tk.Button(
            self.tela_cargas, text="Voltar", command=lambda: self.mostrar_tela(self.tela_menu),
            width=20, height=2
        ).pack(pady=10)

        # Tabela de cargas associadas ao frete
        self.tabela_cargas = ttk.Treeview(self.tela_cargas, columns=("Empresa", "Peso", "Ocupação (%)"), show="headings")
        self.tabela_cargas.pack(fill="both", expand=True)

        self.tabela_cargas.heading("Empresa", text="Empresa")
        self.tabela_cargas.heading("Peso", text="Peso (kg)")
        self.tabela_cargas.heading("Ocupação (%)", text="Ocupação (%)")

        # Define as larguras das colunas
        self.tabela_cargas.column("Empresa", width=200, anchor="center", stretch=tk.YES)
        self.tabela_cargas.column("Peso", width=120, anchor="center", stretch=tk.YES)
        self.tabela_cargas.column("Ocupação (%)", width=120, anchor="center", stretch=tk.YES)

    def adicionar_carga(self):
        """Adiciona uma carga ao frete selecionado."""
        try:
            empresa = self.empresa_entry.get()
            peso = float(self.peso_entry.get())

            # Calcula a ocupação automaticamente
            ocupacao = (peso / self.frete_selecionado["capacidade"]) * 100

            carga = {
                "empresa": empresa,
                "peso": peso,
                "ocupacao": ocupacao
            }

            # Adiciona a carga ao frete selecionado
            self.frete_selecionado["cargas"].append(carga)

            # Atualiza a tabela de cargas
            self.atualizar_lista_cargas()

            # Limpa os campos de entrada
            self.empresa_entry.delete(0, tk.END)
            self.peso_entry.delete(0, tk.END)

        except ValueError:
            print("Erro: Verifique os valores inseridos.")

    def atualizar_lista_fretes(self):
        """Atualiza a tabela de fretes."""
        for item in self.tabela_fretes.get_children():
            self.tabela_fretes.delete(item)

        for frete in self.fretes:
            self.tabela_fretes.insert(
                "", tk.END,
                values=(frete["origem"], frete["destino"], f"{frete['distancia']:.2f}",
                        frete["modelo"], f"{frete['capacidade']:.2f}", frete["tipo"], f"{frete['rendimento']:.2f}",f"{frete['valor']:.2f}",f"{frete['emissao']:.2f}")
            )

    def atualizar_lista_cargas(self):
        """Atualiza a tabela de cargas para o frete selecionado."""
        for item in self.tabela_cargas.get_children():
            self.tabela_cargas.delete(item)

        for carga in self.frete_selecionado["cargas"]:
            self.tabela_cargas.insert(
                "", tk.END,
                values=(carga["empresa"], f"{carga['peso']:.2f}", f"{carga['ocupacao']:.2f}")
            )

# Inicializa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = FreteApp(root)
    root.mainloop()
