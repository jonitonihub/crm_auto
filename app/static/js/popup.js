document.addEventListener("DOMContentLoaded", function () {
    const userInfoBtns = document.querySelectorAll('.user-info-btn');
    const popup = document.getElementById('userInfoPopup');
    const popupContent = document.getElementById('popupContent');
    const closePopup = document.getElementById('closePopup');

    if (!popup || !popupContent) {
        console.error("Попап или его содержимое не найдено в HTML!");
        return;
    }

    // Открытие попапа по кнопке
    userInfoBtns.forEach(function (button) {
        button.addEventListener('click', async function () {
            const userId = button.getAttribute('data-id');
            try {
                const response = await fetch(`/api/user/${userId}`);
                if (!response.ok) throw new Error(`Ошибка: ${response.status}`);

                const user = await response.json();

                // Обновляем содержимое попапа
                popupContent.innerHTML = `
                    <h3>${user.name}</h3>
                    <p>Логин: ${user.login}</p>
                    <p>Статус: ${user.status}</p>
                `;

                // Показываем попап
                popup.style.display = 'flex'; // Используем flex для центрирования
            } catch (error) {
                console.error("Ошибка при загрузке данных:", error);
                alert("Не удалось загрузить данные пользователя.");
            }
        });
    });

    // Закрытие попапа
    closePopup.addEventListener('click', function () {
        popup.style.display = 'none';
    });

    // Закрытие попапа при клике вне его области
    window.addEventListener('click', function (event) {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });
});
