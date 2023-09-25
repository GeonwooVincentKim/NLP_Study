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

## Related Documents & Blog
- https://huggingface.co/datasets/bongsoo/news_talk_en_ko/tree/main
- https://wikidocs.net/22136
- https://metamath1.github.io/blog/posts/gentle-t5-trans/gentle_t5_trans.html
- https://github.com/Beomi/KoAlpaca/blob/main/README.md#koalpaca-korean-alpaca-model-based-on-stanford-alpaca-feat-llama-and-polyglot-ko
- https://github.com/gyupro/Koalpaca-Translation-KR2EN
- https://ooiillppaaiinntt.tistory.com/entry/%EC%9E%90%EC%97%B0%EC%96%B4%EC%B2%98%EB%A6%ACNLP-%EB%AA%A8%EB%8D%B8%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B3%B5%EB%B6%80-%EC%88%9C%EC%84%9C
- https://asecurity.dev/entry/Transformers-GPT-%EC%9D%B4%ED%95%B4
- https://yeong-jin-data-blog.tistory.com/entry/Tranfomer#:~:text=encoder%EB%8A%94%20%EC%9E%85%EB%A0%A5%EB%90%9C%20raw,%2C%20%EB%B9%84%EB%94%94%EC%98%A4)%EB%A1%9C%20%EB%B3%80%ED%99%98%ED%95%9C%EB%8B%A4.
- https://uiandwe.tistory.com/1377
