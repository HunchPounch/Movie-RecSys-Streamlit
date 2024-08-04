[<img src="https://img.shields.io/badge/Streamlit-%40RecSysApp-green">]([https://t.me/StyleTransferPicBot](https://hunchpounch-movie-recsys-recsys-appapp-3r7kil.streamlit.app))

# Movie Recommendation System
## Описание
В данном репозитории представлена [рекомендательная система](https://hunchpounch-movie-recsys-recsys-appapp-3r7kil.streamlit.app), которая подбирает наиболее релеватные фильмы для пользователя по запросу, содержащему название фильма, при помощи машинного обучения. Рекомендации строятся изсходя из косинусных близостей tf-idf векторов, составленных на основе выделенных признаков фильмов, таких как описание, режиссер и т.д. Так же для более продвинутых рекомендаций дополнительно используется ранжирование на основе средневзвешенного рейтинга.


<p align="center">
  <img src="screenshots/app1.png" height="500" alt="Ray Image">
</p>
Написано streamlit приложение, упакованное в Docker и задеплоенное в облако. Ноутбук с обучением находится в репозитории.
