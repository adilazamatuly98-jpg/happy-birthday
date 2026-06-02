import streamlit as st
import time
import random

# Настройка страницы
st.set_page_config(page_title="С днем рождения!", page_icon="💖", layout="centered")

# Инициализация состояния (чтобы переходить по шагам)
if "step" not in st.session_state:
    st.session_state.step = 1

# --- СТИЛИЗАЦИЯ (CSS) ---
st.markdown("""
    <style>
    .reportview-container {
        background: #FFF0F5;
    }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF1493;
        color: white;
    }
    </style>
""", unsafe_with_html=True)

# --- ШАГ 1: ВХОД И АТМОСФЕРА ---
if st.session_state.step == 1:
    st.title("💖 Привет! У меня есть кое-что для тебя...")
    
    # Имитация загрузки сердца
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    
    st.success("Загрузка атмосферы завершена на 100%!")
    
    st.write("### 🎵 Сначала включи этот саундтрек для настроения:")
    # Сюда можно вставить прямую ссылку на mp3 файл (например, из вашего репозитория GitHub)
    # Или использовать iframe для Яндекс.Музыки/Spotify
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") 
    
    st.write("### 🧐 Детектор настроения")
    ready = st.radio("Готова ли ты к сюрпризу?", ("Я еще сомневаюсь...", "Да, покажи мне это!"))
    
    if ready == "Да, покажи мне это!":
        if st.button("Войти в новый мир ✨"):
            st.session_state.step = 2
            st.rerun()

# --- ШАГ 2: ПОЗДРАВЛЕНИЕ И ИИ-ПОРТРЕТЫ ---
elif st.session_state.step == 2:
    st.title("🎉 С Днем Рождения, любимая!")
    
    # Две колонки для сравнения образов
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Как видит тебя мир 🌍")
        # Замените на ваши пути к картинкам в репозитории
        st.image("https://via.placeholder.com/300x400.png?text=World's+View", use_container_width=True) 
    with col2:
        st.subheader("Как вижу тебя я ❤️")
        st.image("https://via.placeholder.com/300x400.png?text=My+View", use_container_width=True)

    st.write("---")
    
    # Эффект печатной машинки
    st.write("### Моё послание тебе:")
    message = "Ты делаешь этот мир ярче каждую секунду. Твоя улыбка — это лучшее, что происходит со мной за день. Сегодня тебе исполняется 22 года, и впереди только самое волшебное..."
    
    placeholder = st.empty()
    typed_text = ""
    for char in message:
        typed_text += char
        placeholder.markdown(f"*{typed_text}*")
        time.sleep(0.04) # Скорость печати
        
    if st.button("Продолжить путешествие ➔"):
        st.session_state.step = 3
        st.rerun()

# --- ШАГ 3: МАГИЧЕСКИЙ ШАР И КОМПЛИМЕНТЫ ---
elif st.session_state.step == 3:
    st.title("🔮 Немного магии и тепла")
    
    st.write("### Что ждет тебя в твои прекрасные 22 года?")
    predictions = [
        "Невероятное путешествие, о котором ты давно мечтала! ✈️",
        "Множество уютных вечеров и теплых объятий. ☕",
        "Творческий прорыв и исполнение главной цели года! 🌟",
        "Много-много поводов для искреннего смеха. 😂"
    ]
    
    if st.button("Спросить Магический Шар 🎱"):
        st.info(random.choice(predictions))
        
    st.write("---")
    st.write("### Лопай пузырьки, чтобы забрать комплименты:")
    
    compliments = {
        "🎈 Пузырек 1": "Ты невероятно умная и проницательная.",
        "🎈 Пузырек 2": "Твоя доброта меняет людей вокруг.",
        "🎈 Пузырек 3": "У тебя потрясающее чувство стиля.",
        "🎈 Пузырек 4": "С тобой тепло даже в самый холодный день."
    }
    
    for key, val in compliments.items():
        if st.checkbox(key):
            st.write(f"✨ *{val}*")
            
    if st.button("Идти дальше ➔"):
        st.session_state.step = 4
        st.rerun()

# --- ШАГ 4: КВИЗ И ОТКРЫТКА ---
elif st.session_state.step == 4:
    st.title("🚪 Стучимся в дверь... Видео-открытка")
    
    # Видео-поздравление
    st.write("Я записал (или подготовил) это для тебя:")
    # Можно вставить ссылку на YouTube, Vimeo или файл в репозитории
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Для теста
    
    st.write("---")
    st.write("### 🧠 Детектор правды: Как хорошо ты меня знаешь?")
    
    q1 = st.radio("Какое моё самое любимое занятие рядом с тобой?", 
                  ("Смотреть фильмы", "Просто обнимать тебя", "Спорить о мелочах"))
    
    if q1 == "Просто обнимать тебя":
        st.success("Абсолютно верно! Ты читаешь мои мысли. ❤️")
    elif q1:
        st.warning("Близко, но объятия все-таки на первом месте! 🤗")
        
    if st.button("Перейти к финалу ➔"):
        st.session_state.step = 5
        st.rerun()

# --- ШАГ 5: ФИНАЛ ---
elif st.session_state.step == 5:
    st.title("🗺️ Наше маленькое приключение")
    st.write("Теперь самое главное. Нам нужно отпраздновать этот день!")
    
    with st.form("celebration_form"):
        st.write("Выбери сценарий, который тебе ближе всего:")
        option = st.selectbox(
            "Куда мы отправимся?",
            ("Романтический ужин в твоем любимом ресторане 🍽️", 
             "Уютный пикник на природе только для двоих 🪵", 
             "Спонтанная поездка на выходные в новый город 🚗", 
             "Твой собственный секретный вариант (расскажешь лично) 🤫")
        )
        
        time_choice = st.time_input("Во сколько мне тебя забрать?")
        notes = st.text_area("Любые пожелания или капризы на сегодня:")
        
        submitted = st.form_submit_button("Утвердить план празднования! 💌")
        if submitted:
            st.balloons()
            st.success("Ура! План принят!")
            st.write(f"Ты выбрала: **{option}**")
            st.write(f"Время встречи: **{time_choice}**")
            if notes:
                st.write(f"Твои пожелания: *{notes}*")
            st.write("👉 Сделай скриншот этого экрана и отправь мне, я уже готовлюсь! 😘")
            
    if st.button("Начать сначала ↺"):
        st.session_state.step = 1
        st.rerun()