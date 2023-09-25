# Transformer Architecture
> Let's get to know what is Transformer Architecture is

## Pre-train & Fine-Tuning

### Pre-train
- 일반적인 지식을 얻는 방법
  + 책이나 다양한 매체 등을 통해 학습하는 것
  + 아무 것도 모르는 학생들을 유치원부터 시작하여 초, 중, 고등학교를 차례대로 졸업까지 시키는 과정을 의미함

- BERT 가 문맥 정보를 갖고 빈칸 맞추기 하는 과정

### Fine-Tuning
- 감정 분류나 번역 모델 학습 등과 같은 곳에서 활용
  + 고등학교 졸업 이후, 대학에 가서 전공 지식을 배우는 과정을 의미함

- 학습이 끝난 BERT 를 가지고 감정 분류, 또는 여러 모델들을 활용하여 학습
  + 일반적인 지식을 갖고 있는 (Pre-trained) 모델에 관심있는 Task 에 적용하는 것

## Encoder & Decoder

### Encoder
- 암호화
  + Masking
  + BERT 계열

### Decoder
- 복호화
  + 생성하는 느낌
  + GPT 계열
