# kaggle을 이용한 데이터셋 다운로드
from google.colab import files 
files.upload()  # kaggle
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d phylake1337/fire-dataset
!unzip fire-dataset.zip -d /content/dataset
# 이미지 데이터 전처리
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_generator = train_datagen.flow_from_directory('/content/dataset/fire_dataset', target_size=(150, 150), batch_size=32, class_mode='binary', subset='training')
validation_generator = train_datagen.flow_from_directory( '/content/dataset/fire_dataset', target_size=(150, 150), batch_size=32, class_mode='binary', subset='validation')
# 모델 만들기
from tensorflow.keras import layers, models
model = models.Sequential([ layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)), layers.MaxPooling2D(2, 2), layers.Conv2D(64, (3, 3), activation='relu'), layers.MaxPooling2D(2, 2), layers.Conv2D(128, (3, 3), activation='relu'), layers.MaxPooling2D(2, 2), layers.Flatten(),  layers.Dense(512, activation='relu'), layers.Dense(1, activation='sigmoid')])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# 모델 학습
history = model.fit(
    train_generator,
    steps_per_epoch=100,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=50)
