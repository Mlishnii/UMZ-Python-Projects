import tkinter as tk
import random
from tkinter import messagebox, simpledialog
import sqlite3

conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    instructions TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    unit TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS recipe_ingredients (
    recipe_id INTEGER,
    ingredient_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES recipes (id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients (id)
)
''')

conn.commit()


recipes = []

ingredients = []

def clear_main_window():
    for widget in root.winfo_children():
        widget.destroy()

def show_main_page():
    clear_main_window()
    create_main_page()

def create_main_page():
    root.title("مدیریت دستورهای غذایی")


    btn_recipe = tk.Button(root, text="دستور غذایی", command=show_recipe_page)
    btn_recipe.pack(pady=10)

    btn_ingredients = tk.Button(root, text="مواد غذایی", command=show_ingredients_page)
    btn_ingredients.pack(pady=10)

    btn_suggested_recipes = tk.Button(root, text="دستور پیشنهادی", command=show_suggested_recipes_page)
    btn_suggested_recipes.pack(pady=10)

    btn_weekly_plan = tk.Button(root, text="برنامه هفتگی", command=show_weekly_plan_page)
    btn_weekly_plan.pack(pady=10)

def show_recipe_page():
    clear_main_window()


    lbl_title = tk.Label(root, text="مدیریت دستور غذایی", font=("Helvetica", 18))
    lbl_title.pack(pady=10)


    btn_add_recipe = tk.Button(root, text="افزودن دستور غذایی", command=add_recipe)
    btn_add_recipe.pack()


    btn_edit_recipe = tk.Button(root, text="ویرایش دستور غذایی", command=edit_recipe)
    btn_edit_recipe.pack()


    btn_delete_recipe = tk.Button(root, text="حذف دستور غذایی", command=delete_recipe)
    btn_delete_recipe.pack()

    btn_view_recipes = tk.Button(root, text="مشاهده دستور غذایی", command=view_recipes)
    btn_view_recipes.pack()

    btn_back = tk.Button(root, text="بازگشت به صفحه اصلی", command=show_main_page)
    btn_back.pack(pady=20)
def view_recipes():
    view_window = tk.Toplevel(root)
    view_window.title("مشاهده دستورهای غذایی")

    cursor.execute('''
    SELECT r.name, r.instructions, i.name, ri.amount, i.unit
    FROM recipes r
    LEFT JOIN recipe_ingredients ri ON r.id = ri.recipe_id
    LEFT JOIN ingredients i ON ri.ingredient_id = i.id
    ''')
    recipes_data = cursor.fetchall()

    if recipes_data:
        current_recipe = None
        recipe_text = ""

        for row in recipes_data:
            name, instructions, ingredient_name, amount, unit = row
            if current_recipe != name:
                if current_recipe is not None:
                    lbl_recipe = tk.Label(view_window, text=recipe_text, justify=tk.LEFT)
                    lbl_recipe.pack(pady=5)
                current_recipe = name
                recipe_text = f"نام: {name}\nطرز تهیه: {instructions}\nمواد:\n"

            recipe_text += f"- {ingredient_name} ({amount} {unit})\n"

        if recipe_text:
            lbl_recipe = tk.Label(view_window, text=recipe_text, justify=tk.LEFT)
            lbl_recipe.pack(pady=5)
    else:
        lbl_no_recipes = tk.Label(view_window, text="هیچ دستوری موجود نیست.", justify=tk.LEFT)
        lbl_no_recipes.pack(pady=5)
def add_recipe():
    add_window = tk.Toplevel(root)
    add_window.title("افزودن دستور غذایی")

    lbl_name = tk.Label(add_window, text="نام دستور غذایی:")
    lbl_name.pack()
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    lbl_instructions = tk.Label(add_window, text="طرز تهیه:")
    lbl_instructions.pack()
    entry_instructions = tk.Text(add_window, height=10)
    entry_instructions.pack()

    lbl_ingredients = tk.Label(add_window, text="مواد غذایی:")
    lbl_ingredients.pack()
    ingredient_vars = []
    cursor.execute('SELECT id, name, unit FROM ingredients')
    ingredients = cursor.fetchall()
    for ingredient in ingredients:
        var = tk.BooleanVar()
        amount = tk.StringVar(value="1")
        frame = tk.Frame(add_window)
        chk = tk.Checkbutton(frame, text=ingredient[1], variable=var)
        chk.pack(side=tk.LEFT)
        entry_amount = tk.Entry(frame, textvariable=amount, width=5)
        entry_amount.pack(side=tk.RIGHT)
        frame.pack()
        ingredient_vars.append((ingredient, var, amount))

    def save_recipe():
        name = entry_name.get()
        instructions = entry_instructions.get("1.0", tk.END).strip()
        selected_ingredients = [{"id": ingredient[0], "amount": int(amount.get())} for ingredient, var, amount in ingredient_vars if var.get()]

        if name and instructions and selected_ingredients:
            cursor.execute('INSERT INTO recipes (name, instructions) VALUES (?, ?)', (name, instructions))
            recipe_id = cursor.lastrowid
            for ingredient in selected_ingredients:
                cursor.execute('INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES (?, ?, ?)', (recipe_id, ingredient["id"], ingredient["amount"]))
            conn.commit()
            tk.messagebox.showinfo("افزودن دستور غذایی", f"دستور غذایی '{name}' با موفقیت اضافه شد.")
            add_window.destroy()
            show_recipe_page()
        else:
            tk.messagebox.showerror("خطا", "لطفاً تمامی فیلدها را پر کنید و حداقل یک ماده غذایی انتخاب کنید.")

    btn_save = tk.Button(add_window, text="ذخیره", command=save_recipe)
    btn_save.pack(pady=10)

def edit_recipe():
    edit_window = tk.Toplevel(root)
    edit_window.title("ویرایش دستور غذایی")

    lbl_name = tk.Label(edit_window, text="نام دستور غذایی:")
    lbl_name.pack()
    entry_name = tk.Entry(edit_window)
    entry_name.pack()

    def load_recipe():
        name = entry_name.get()
        cursor.execute('SELECT id, instructions FROM recipes WHERE name = ?', (name,))
        recipe = cursor.fetchone()
        if recipe:
            recipe_id = recipe[0]
            entry_name.config(state='disabled')
            entry_instructions.delete("1.0", tk.END)
            entry_instructions.insert(tk.END, recipe[1])

            cursor.execute('SELECT ingredient_id, amount FROM recipe_ingredients WHERE recipe_id = ?', (recipe_id,))
            recipe_ingredients = cursor.fetchall()
            recipe_ingredient_dict = {item[0]: item[1] for item in recipe_ingredients}

            for ingredient, var, amount in ingredient_vars:
                if ingredient[0] in recipe_ingredient_dict:
                    var.set(True)
                    amount.set(recipe_ingredient_dict[ingredient[0]])
                else:
                    var.set(False)
                    amount.set("1")

            def save_recipe():
                instructions = entry_instructions.get("1.0", tk.END).strip()
                selected_ingredients = [{"id": ingredient[0], "amount": int(amount.get())} for ingredient, var, amount in ingredient_vars if var.get()]

                if instructions and selected_ingredients:
                    cursor.execute('UPDATE recipes SET instructions = ? WHERE id = ?', (instructions, recipe_id))
                    cursor.execute('DELETE FROM recipe_ingredients WHERE recipe_id = ?', (recipe_id,))
                    for ingredient in selected_ingredients:
                        cursor.execute('INSERT INTO recipe_ingredients (recipe_id, ingredient_id, amount) VALUES (?, ?, ?)', (recipe_id, ingredient["id"], ingredient["amount"]))
                    conn.commit()
                    tk.messagebox.showinfo("ویرایش دستور غذایی", f"دستور غذایی '{name}' با موفقیت ویرایش شد.")
                    edit_window.destroy()
                    show_recipe_page()
                else:
                    tk.messagebox.showerror("خطا", "لطفاً تمامی فیلدها را پر کنید و حداقل یک ماده غذایی انتخاب کنید.")

            btn_save.config(command=save_recipe)
        else:
            tk.messagebox.showerror("خطا", f"دستور غذایی با نام '{name}' یافت نشد.")

    btn_load = tk.Button(edit_window, text="بارگذاری دستور غذایی", command=load_recipe)
    btn_load.pack(pady=10)

    lbl_instructions = tk.Label(edit_window, text="طرز تهیه:")
    lbl_instructions.pack()
    entry_instructions = tk.Text(edit_window, height=10)
    entry_instructions.pack()

    lbl_ingredients = tk.Label(edit_window, text="مواد غذایی:")
    

    lbl_ingredients.pack()
    ingredient_vars = []
    cursor.execute('SELECT id, name, unit FROM ingredients')
    ingredients = cursor.fetchall()
    for ingredient in ingredients:
        var = tk.BooleanVar()
        amount = tk.StringVar(value="1")
        frame = tk.Frame(edit_window)
        chk = tk.Checkbutton(frame, text=ingredient[1], variable=var)
        chk.pack(side=tk.LEFT)
        entry_amount = tk.Entry(frame, textvariable=amount, width=5)
        entry_amount.pack(side=tk.RIGHT)
        frame.pack()
        ingredient_vars.append((ingredient, var, amount))

    btn_save = tk.Button(edit_window, text="ذخیره")
    btn_save.pack(pady=10)

def delete_recipe():
    recipe_name = tk.simpledialog.askstring("حذف دستور غذایی", "نام دستور غذایی مورد نظر:")
    if recipe_name:
        cursor.execute('SELECT id FROM recipes WHERE name = ?', (recipe_name,))
        recipe = cursor.fetchone()
        if recipe:
            cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe[0],))
            cursor.execute('DELETE FROM recipe_ingredients WHERE recipe_id = ?', (recipe[0],))
            conn.commit()
            tk.messagebox.showinfo("حذف دستور غذایی", f"دستور غذایی '{recipe_name}' با موفقیت حذف شد.")
            show_recipe_page()
        else:
            tk.messagebox.showerror("خطا", f"دستور غذایی با نام '{recipe_name}' یافت نشد.")
def show_ingredients_page():
    clear_main_window()

    lbl_title = tk.Label(root, text="مدیریت مواد غذایی", font=("Helvetica", 18))
    lbl_title.pack(pady=10)
    btn_add_ingredient = tk.Button(root, text="افزودن ماده غذایی", command=add_ingredient)
    btn_add_ingredient.pack()
    btn_edit_ingredient = tk.Button(root, text="ویرایش ماده غذایی", command=edit_ingredient)
    btn_edit_ingredient.pack()

    btn_delete_ingredient = tk.Button(root, text="حذف ماده غذایی", command=delete_ingredient)
    btn_delete_ingredient.pack()

    btn_view_ingredients = tk.Button(root, text="مشاهده مواد غذایی", command=view_ingredients)
    btn_view_ingredients.pack()

    btn_back = tk.Button(root, text="بازگشت به صفحه اصلی", command=show_main_page)
    btn_back.pack(pady=20)
def view_ingredients():
    view_window = tk.Toplevel(root)
    view_window.title("مشاهده مواد غذایی")

    cursor.execute('SELECT name, unit FROM ingredients')
    ingredients = cursor.fetchall()

    for ingredient in ingredients:
        ingredient_text = f"نام: {ingredient[0]}\nواحد: {ingredient[1]}\n"
        lbl_ingredient = tk.Label(view_window, text=ingredient_text, justify=tk.LEFT)
        lbl_ingredient.pack(pady=5)

def add_ingredient():
    add_window = tk.Toplevel(root)
    add_window.title("افزودن ماده غذایی")

    lbl_name = tk.Label(add_window, text="نام ماده غذایی:")
    lbl_name.pack()
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    lbl_unit = tk.Label(add_window, text="واحد:")
    lbl_unit.pack()
    entry_unit = tk.Entry(add_window)
    entry_unit.pack()

    def save_ingredient():
        name = entry_name.get()
        unit = entry_unit.get()

        if name and unit:
            cursor.execute('INSERT INTO ingredients (name, unit) VALUES (?, ?)', (name, unit))
            conn.commit()
            tk.messagebox.showinfo("افزودن ماده غذایی", f"ماده غذایی '{name}' با موفقیت اضافه شد.")
            add_window.destroy()
            show_ingredients_page()
        else:
            tk.messagebox.showerror("خطا", "لطفاً تمامی فیلدها را پر کنید.")

    btn_save = tk.Button(add_window, text="ذخیره", command=save_ingredient)
    btn_save.pack(pady=10)
def edit_ingredient():
    edit_window = tk.Toplevel(root)
    edit_window.title("ویرایش ماده غذایی")

    lbl_name = tk.Label(edit_window, text="نام ماده غذایی:")
    lbl_name.pack()
    entry_name = tk.Entry(edit_window)
    entry_name.pack()

    def load_ingredient():
        name = entry_name.get()
        cursor.execute('SELECT id, unit FROM ingredients WHERE name = ?', (name,))
        ingredient = cursor.fetchone()
        if ingredient:
            entry_name.config(state='disabled')
            entry_unit.delete(0, tk.END)
            entry_unit.insert(0, ingredient[1])

            def save_ingredient():
                unit = entry_unit.get()
                if unit:
                    cursor.execute('UPDATE ingredients SET unit = ? WHERE id = ?', (unit, ingredient[0]))
                    conn.commit()
                    tk.messagebox.showinfo("ویرایش ماده غذایی", f"ماده غذایی '{name}' با موفقیت ویرایش شد.")
                    edit_window.destroy()
                    show_ingredients_page()
                else:
                    tk.messagebox.showerror("خطا", "لطفاً تمامی فیلدها را پر کنید.")

            btn_save.config(command=save_ingredient)
        else:
            tk.messagebox.showerror("خطا", f"ماده غذایی با نام '{name}' یافت نشد.")

    btn_load = tk.Button(edit_window, text="بارگذاری ماده غذایی", command=load_ingredient)
    btn_load.pack(pady=10)

    lbl_unit = tk.Label(edit_window, text="واحد:")
    lbl_unit.pack()
    entry_unit = tk.Entry(edit_window)
    entry_unit.pack()

    btn_save = tk.Button(edit_window, text="ذخیره")
    btn_save.pack(pady=10)

def delete_ingredient():
    ingredient_name = tk.simpledialog.askstring("حذف ماده غذایی", "نام ماده غذایی مورد نظر:")
    if ingredient_name:
        cursor.execute('SELECT id FROM ingredients WHERE name = ?', (ingredient_name,))
        ingredient = cursor.fetchone()
        if ingredient:
            cursor.execute('DELETE FROM ingredients WHERE id = ?', (ingredient[0],))
            cursor.execute('DELETE FROM recipe_ingredients WHERE ingredient_id = ?', (ingredient[0],))
            conn.commit()
            tk.messagebox.showinfo("حذف ماده غذایی", f"ماده غذایی '{ingredient_name}' با موفقیت حذف شد.")
            show_ingredients_page()
        else:
            tk.messagebox.showerror("خطا", f"ماده غذایی با نام '{ingredient_name}' یافت نشد.")

def show_suggested_recipes_page():
    clear_main_window()

    lbl_title = tk.Label(root, text="دستور پیشنهادی", font=("Helvetica", 18))
    lbl_title.pack(pady=10)

    lbl_ingredients = tk.Label(root, text="مواد غذایی:")
    lbl_ingredients.pack()
    ingredient_vars = []
    cursor.execute('SELECT name FROM ingredients')
    all_ingredients = cursor.fetchall()

    for ingredient in all_ingredients:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(root, text=ingredient[0], variable=var)
        chk.pack()
        ingredient_vars.append((ingredient[0], var))

    def suggest_recipe():
        selected_ingredients = {ingredient for ingredient, var in ingredient_vars if var.get()}
        if not selected_ingredients:
            tk.messagebox.showinfo("خطا", "لطفاً حداقل یک ماده غذایی انتخاب کنید.")
            return

        cursor.execute('''
        SELECT r.id, r.name, r.instructions
        FROM recipes r
        JOIN recipe_ingredients ri ON r.id = ri.recipe_id
        JOIN ingredients i ON ri.ingredient_id = i.id
        WHERE i.name IN ({})
        GROUP BY r.id, r.name, r.instructions
        HAVING COUNT(DISTINCT i.name) = (
            SELECT COUNT(DISTINCT i2.name)
            FROM recipe_ingredients ri2
            JOIN ingredients i2 ON ri2.ingredient_id = i2.id
            WHERE ri2.recipe_id = r.id
        )
        '''.format(','.join('?' for _ in selected_ingredients)), list(selected_ingredients))

        possible_recipes = cursor.fetchall()

        if possible_recipes:
            suggested_recipe = random.choice(possible_recipes)
            recipe_id, recipe_name, recipe_instructions = suggested_recipe

            cursor.execute('''
            SELECT i.name, ri.amount, i.unit
            FROM recipe_ingredients ri
            JOIN ingredients i ON ri.ingredient_id = i.id
            WHERE ri.recipe_id = ?
            ''', (recipe_id,))
            recipe_ingredients = cursor.fetchall()

            recipe_text = f"دستور غذایی پیشنهادی:\nنام: {recipe_name}\nطرز تهیه: {recipe_instructions}\nمواد:\n"
            for ingredient_name, amount, unit in recipe_ingredients:
                recipe_text += f"- {ingredient_name} ({amount} {unit})\n"
            tk.messagebox.showinfo("دستور غذایی پیشنهادی", recipe_text)
        else:
            tk.messagebox.showinfo("دستور غذایی پیشنهادی", "هیچ دستور غذایی متناسب با مواد غذایی انتخاب شده یافت نشد.")

    btn_suggest = tk.Button(root, text="پیشنهاد دستور غذایی", command=suggest_recipe)
    btn_suggest.pack(pady=10)

    btn_back = tk.Button(root, text="بازگشت به صفحه اصلی", command=show_main_page)
    btn_back.pack(pady=20)

def show_weekly_plan_page():
    clear_main_window()

    lbl_title = tk.Label(root, text="برنامه هفتگی", font=("Helvetica", 18))
    lbl_title.pack(pady=10)

    def generate_weekly_plan():
        cursor.execute('SELECT id, name, instructions FROM recipes')
        recipes = cursor.fetchall()

        if not recipes:
            tk.messagebox.showerror("خطا", "هیچ دستوری غذایی وجود ندارد.")
            return

        weekly_plan = []
        for i in range(7):
            daily_meal = random.choice(recipes)
            weekly_plan.append(daily_meal)

        plan_text = "برنامه هفتگی:\n"
        shopping_list = {}

        for i, meal in enumerate(weekly_plan):
            plan_text += f"روز {i + 1}: {meal[1]}\n"
            cursor.execute('''
            SELECT i.name, ri.amount, i.unit 
            FROM recipe_ingredients ri
            JOIN ingredients i ON ri.ingredient_id = i.id
            WHERE ri.recipe_id = ?
            ''', (meal[0],))
            ingredients = cursor.fetchall()

            for ingredient in ingredients:
                if ingredient[0] in shopping_list:
                    shopping_list[ingredient[0]]["amount"] += ingredient[1]
                else:
                    shopping_list[ingredient[0]] = {"unit": ingredient[2], "amount": ingredient[1]}

        plan_text += "\nلیست خرید:\n"
        for ingredient, details in shopping_list.items():
            plan_text += f"- {ingredient}: {details['amount']} {details['unit']}\n"

        tk.messagebox.showinfo("برنامه هفتگی", plan_text)

    btn_generate_plan = tk.Button(root, text="تولید برنامه هفتگی", command=generate_weekly_plan)
    btn_generate_plan.pack(pady=10)

    btn_back = tk.Button(root, text="بازگشت به صفحه اصلی", command=show_main_page)
    btn_back.pack(pady=20)

root = tk.Tk()
create_main_page()

root.mainloop()

