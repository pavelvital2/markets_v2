# Единое ТЗ на продукт Market Intelligence Platform

**Версия:** 1.0  
**Дата:** 12.05.2026  
**Назначение:** входной продуктовый документ для проектирования и реализации системы.

---

## 1. Суть проекта

Нужно создать систему **Market Intelligence Platform** для анализа внешнего рынка WB и Ozon, а в следующих этапах — для сопоставления внешнего рынка с собственными товарами и кабинетами продавца.

Система должна состоять из двух новых независимых проектов:

1. **`market-parser-v2`** — новый чистый объединённый парсер внешнего рынка WB + Ozon.
2. **`market-analytics`** — новая аналитическая программа, создаваемая с нуля.

Существующие рабочие парсеры используются только как источники фактической реализации, контрактов и проверенных подходов. Их нельзя ломать, переносить или менять без отдельного решения.

---

## 2. Цель продукта

Продукт должен отвечать на практические бизнес-вопросы:

- какие поисковые запросы на WB и Ozon перспективны;
- какие товары и продавцы занимают выдачу;
- где конкуренция слабая или сильная;
- где видны рыночные возможности;
- где наши товары есть или отсутствуют в выдаче после подключения own-store данных;
- где нужно менять цену, SEO, ассортимент, остатки или продвижение;
- какие изменения произошли на рынке между запусками парсера;
- насколько можно доверять данным конкретного запуска.

Главная ценность продукта — не хранение CSV-выгрузок, а понятные управленческие выводы и действия.

---

## 3. Источники фактов и рабочие проекты

| Источник | Ссылка / путь | Роль в новом проекте |
|---|---|---|
| WB parser | `/home/pavel/projects/wb-parser-v1` | Read-only источник WB-логики, контрактов, outputs, подходов к suggest/filter/serp/sellers, run reports и data layers. |
| Ozon parser | `/home/pavel/projects/parser_ozon` | Read-only источник Ozon-логики, Playwright/Chromium flow, extraction rules, outputs и tests. |
| Документация Ozon parser | `/home/pavel/projects/parser_ozon/docs/ozon_parser/` | Read-only источник описания Ozon endpoints, data contracts, operations и проверенного состояния прототипа. |

Минимально важные файлы WB-парсера для обследования:

- `README.md`;
- `ARCHITECTURE.md`;
- `PROJECT_STATE.md`;
- `DEVELOPMENT_STAGES.md`;
- `app/suggest/alpha.py`;
- `app/filter/engine.py`;
- `app/serp/engine.py`;
- `app/sellers/engine.py`;
- `app/common/paths.py`;
- `app/common/csv_io.py`;
- `app/common/runner.py`;
- `state/run_reports/latest.json`.

Минимально важные файлы Ozon-парсера для обследования:

- `package.json`;
- `scripts/collect_ozon_suggest.js`;
- `scripts/collect_ozon_products.js`;
- `scripts/enrich_ozon_sellers.js`;
- `scripts/collect_ozon_network.js`;
- `ozon_parser/extractor.py`;
- `ozon_parser/suggest_extractor.py`;
- `tests/test_ozon_extractor.py`;
- `tests/test_ozon_suggest_extractor.py`;
- `docs/ozon_parser/*`, если документация есть в проекте.

---

## 4. Границы продукта

### 4.1. Что входит

В продукт входят:

- сбор данных внешнего рынка WB;
- сбор данных внешнего рынка Ozon;
- унификация данных WB/Ozon на уровне контрактов и аналитических витрин;
- отдельная аналитическая программа с веб-интерфейсом;
- импорт данных из parser export bundle;
- хранение истории запусков;
- витрины по запросам, товарам, продавцам, позициям, ценам, рейтингам, отзывам и качеству данных;
- Excel-экспорт;
- архитектурная подготовка к подключению личных кабинетов WB/Ozon;
- архитектурная подготовка к единому справочнику собственных товаров;
- архитектурная подготовка к Decision Layer.

### 4.2. Что не входит в первую рабочую версию продукта

В первую рабочую версию не входят как подтверждённые расчёты:

- точная прибыль;
- точная маржа;
- фактическая выручка;
- продажи конкурентов;
- рекламная эффективность;
- конверсия карточки;
- точная себестоимость;
- точная экономика поставки.

Эти расчёты допустимы только после подключения подтверждённых источников: продаж, заказов, остатков, себестоимости, комиссий, логистики, рекламы, возвратов и финансовых отчётов.

---

## 5. Компоненты продукта

Продукт состоит из двух новых независимых компонентов:

1. **`market-parser-v2`** — сбор и подготовка данных внешнего рынка WB/Ozon.
2. **`market-analytics`** — аналитика, веб-интерфейс, импорт данных, витрины, история, Excel-экспорт и будущий Decision Layer.

Код продукта, данные, логи, секреты, cookies, raw archives и временные файлы должны храниться раздельно. Данные, логи, cookies, секреты и raw archives не должны попадать в Git.

---

## 6. `market-parser-v2`: назначение и требования

### 6.1. Назначение

`market-parser-v2` отвечает только за сбор и подготовку данных внешнего рынка WB/Ozon. Он не должен быть аналитической программой и не должен хранить бизнес-логику Decision Layer.

### 6.2. Общая архитектурная идея

Новый парсер создаётся как чистый provider-aware компонент. Логические зоны:

1. Common core: запуск, конфигурация, state, reports, logging, checkpoints, export.
2. WB provider: сбор и нормализация WB-данных.
3. Ozon provider: сбор и нормализация Ozon-данных.

Допустимая логика pipeline:

```text
suggest -> filter -> serp -> sellers -> export
```

Компоненты должны применяться только там, где они подтверждены для конкретного маркетплейса.

### 6.3. Обязательные возможности парсера

Парсер должен поддерживать:

- запуск по маркетплейсу: `wb`, `ozon`, `all`;
- компоненты `suggest`, `filter`, `serp`, `sellers`, где применимо;
- слои `raw`, `staging`, `marts`;
- уникальный `run_id` для каждого запуска;
- `latest`-зеркала для последних данных;
- run reports;
- checkpoints/resume;
- contract validation;
- CSV encoding `utf-8-sig`;
- CSV delimiter `;` там, где сохраняется совместимость с WB;
- provider-specific raw/staging данные;
- common marts для аналитики;
- стабильный export bundle для `market-analytics`.

### 6.4. Общие сервисные поля

В outputs должны использоваться сервисные поля, если они применимы к конкретной сущности:

```text
run_id
component
collected_at_utc
source_system
source_type
source_ref
status
error_message
schema_version
```

Для WB:

```text
source_system = wb
```

Для Ozon:

```text
source_system = ozon
```

WB и Ozon identifiers локальны внутри маркетплейса. Нельзя соединять WB `nmId` и Ozon product id без `source_system`/`marketplace`.

Рекомендуемые универсальные ключи:

```text
source_system + external_product_id
source_system + external_seller_id
source_system + query
```

Если для совместимости временно используется поле `nmId` под Ozon product id, это должно быть явно описано в контракте и не должно трактоваться как WB `nmId`.

---

## 7. WB-часть парсера

WB-часть должна опираться на фактический проект:

```text
/home/pavel/projects/wb-parser-v1
```

Подтверждаемая архитектурная база WB:

- components: `suggest`, `filter`, `serp`, `sellers`;
- pipelines: `monthly`, `daily`;
- storage: `raw`, `staging`, `marts`;
- `run_id`;
- latest mirrors;
- run reports;
- export files: `queries.txt`, `products_for_sellers.csv`, `products_daily_preview.csv`;
- CSV format: `utf-8-sig`, delimiter `;`.

Перед переносом логики нужно подтвердить фактические поля CSV/JSON, команды запуска, state/checkpoints, retry/backoff, web UI, тесты, ошибки и статусы.

---

## 8. Ozon-часть парсера

Ozon-часть должна опираться на фактический проект:

```text
/home/pavel/projects/parser_ozon
```

### 8.1. Подтверждённые ориентиры Ozon-прототипа

Ориентиры из документации Ozon-прототипа, которые нужно проверить по фактическому коду и outputs:

- прототип собирает `suggest`, `products/serp` и `sellers`;
- текущие scripts: `collect_ozon_suggest.js`, `collect_ozon_products.js`, `enrich_ozon_sellers.js`, `collect_ozon_network.js`;
- есть Python extractors/tests: `ozon_parser/extractor.py`, `ozon_parser/suggest_extractor.py`, `tests/*`;
- по проверенному запуску из документации: query `шеврон на липучке`, 1000 product rows, 125 Ozon pagination portions, 8 product tiles per desktop response, 120 unique sellers, 1000 bridge rows;
- seller enrichment заполняет `supplier_id` и `supplier_name` через product card HTML state;
- seller bridge связывает query, product и seller.

Эти факты не являются вечными гарантиями Ozon и должны быть валидированы при разработке.

### 8.2. Ozon suggest

Ozon suggest должен:

- использовать endpoint через Chromium/browser session;
- читать base prefixes из конфигурации;
- обрабатывать seed query и `prefix + Russian letter`;
- извлекать поисковые подсказки из `widgetStates["webSuggestions-*"]`;
- брать только первые 5 dropdown suggestions как поисковые запросы;
- не включать позиции после 5, если это category/brand/store/ad suggestions;
- писать raw/staging/filter outputs по утверждённому контракту;
- формировать `queries.txt` для дальнейшего SERP-сбора.

Возможное дополнительное правило для production:

```text
position <= 5 AND action.link starts with /search/
```

### 8.3. Ozon SERP/products

Ozon SERP должен учитывать:

- публичный URL поиска может редиректить в category page;
- page 1 может быть embedded в initial HTML state;
- page 2+ загружаются через `/api/entrypoint-api.bx/page/json/v2`;
- пагинация идёт через `nextPage`;
- `nextPage`, `paginator_token`, `search_page_state`, `start_page_id` нужно считать opaque state;
- нельзя синтезировать Ozon pagination tokens;
- product grid находится в `widgetStates["tileGridDesktop-*"]`;
- observed desktop page size = 8, но финальный код должен использовать фактическое `items.length`, а не вечную константу;
- analytics compatibility должна использовать `absolute_position`, а не provider page number.

### 8.4. Ozon sellers

Ozon SERP tileGrid не содержит seller data. Seller enrichment должен:

- получать product card URL из tile `action.link`;
- читать seller state из initial product HTML: `state-webCurrentSeller-*`;
- загружать только HTML document;
- блокировать scripts, XHR, images, media, fonts, CSS при seller enrichment;
- извлекать seller id/name/rating/reviews best-effort;
- заполнять seller fields в product marts или отдельном enriched mart;
- писать sellers mart и seller-query-product bridge;
- поддерживать progress/resume, так как product-card visits являются медленной и block-sensitive частью.

### 8.5. Ozon security and stability

Обязательные правила:

- Ozon cookie задаётся через env/path, например `OZON_COOKIE_FILE`;
- cookies нельзя коммитить, логировать, сохранять в fixtures или показывать в UI;
- HAR/fixtures должны быть sanitized;
- при anti-bot/empty pages запуск должен останавливаться или переходить в partial/failure с понятным статусом;
- concurrency/throttle должны быть настраиваемыми.

---

## 9. Основные data contracts

Точные поля должны быть подтверждены по source projects и sample data. Минимально ожидаемые контракты:

### 9.1. Query / suggest / filter

- raw suggest rows;
- staging suggest rows;
- ranked `top_queries.csv`;
- `queries.txt` как список нормализованных запросов;
- query grouping / canonical query, если подтверждено или реализовано в filter.

Ожидаемые поля для query analytics:

```text
marketplace
query
normalized_query
canonical_query
query_group
source_query
rank
score / hybrid_score
wordstat_volume, если подтверждено
count
selected_reason
```

### 9.2. Products / SERP

Ожидаемые поля для product marts:

```text
marketplace
source_system
run_id
query
query_group
page
position_on_page
absolute_position
external_product_id
product_name
brand
external_seller_id
seller_name
final_price
price
old_price / sale_price, если подтверждено
rating
reviews_count / feedbacks
promo_markers
raw_file
raw_page_path
data_quality_status
```

Для WB поле `external_product_id` может соответствовать `nmId`. Для Ozon оно должно соответствовать подтверждённому Ozon product id / sku / offer id.

### 9.3. Sellers

Ожидаемые поля для seller marts:

```text
marketplace
source_system
run_id
external_seller_id
seller_name
seller_rating, если есть
seller_reviews / feedbacks_count, если есть
product_count
query_count
queries_ref
query_groups_ref
external_product_ids_ref
source_product_run_ids
data_quality_status
```

### 9.4. Seller-query-product bridge

Bridge нужен для связи запроса, товара и продавца:

```text
marketplace
source_system
run_id
query
query_group
external_product_id
external_seller_id
seller_name
product_run_id
```

### 9.5. Data quality

Должны фиксироваться:

- partial runs;
- errors per component;
- missing pages;
- empty products;
- missing seller id;
- duplicate product positions;
- unexpected CSV columns;
- schema version mismatch;
- checksum mismatch;
- stale latest export.

Рекомендуемые статусы использования данных:

```text
valid_for_reports
partial_use_with_warning
invalid_for_reports
```

---

## 10. Export contract parser -> analytics

`market-analytics` не должна читать внутренние папки парсера напрямую в промышленном режиме.

Основной канал данных — стабильный export bundle:

```text
market-parser-v2 analytics export:
  latest.json
  {marketplace}/{run_id}/manifest.json
  {marketplace}/{run_id}/bundle.tar.gz
  {marketplace}/{run_id}/checksums.sha256
```

`manifest.json` должен содержать минимум:

- marketplace/source_system;
- run_id;
- schema_version;
- export_created_at_utc;
- component statuses;
- file list;
- row counts;
- checksums;
- data quality summary;
- whether run is usable for reports;
- warnings/errors.

`bundle.tar.gz` должен содержать только файлы, необходимые аналитике. Секреты, cookies, raw sensitive fixtures и рабочие логи не должны попадать в bundle.

---

## 11. `market-analytics`: назначение и требования

### 11.1. Назначение

`market-analytics` создаётся с нуля как отдельная программа. Она отвечает за импорт, хранение, анализ, визуализацию и экспорт аналитики.

Первый обязательный контур — **Market Intelligence** по внешним данным WB/Ozon из `market-parser-v2`.

Будущие контуры:

- **Own Store Intelligence** — данные личных кабинетов WB/Ozon и внутренние справочники;
- **Product Matching** — связь физических товаров с listings WB/Ozon;
- **Decision Layer** — управленческие сигналы и рекомендации.

### 11.2. Базовая техническая схема

Рекомендуемый базовый стек:

```text
Python + FastAPI + PostgreSQL + web UI + worker/scheduler + systemd + Nginx в целевой схеме
```

Альтернативный стек допустим, если он покрывает требования импорта, хранения истории, API, UI, Excel-экспорта, авторизации и эксплуатации.

### 11.3. Импорт

Аналитика должна:

- импортировать parser export bundle;
- проверять manifest и checksums;
- хранить imported run registry;
- сохранять все `run_id`, а не только latest;
- учитывать marketplace/source_system;
- маркировать качество данных;
- предупреждать пользователя о partial data;
- не смешивать WB/Ozon identifiers без provider context.

---

## 12. Market Intelligence MVP

### 12.1. Главный экран

Главный экран должен быть управленческой панелью, а не одной большой таблицей.

Обязательные элементы:

- переключатель marketplace: WB / Ozon / оба;
- период анализа;
- дата последнего обновления;
- статус последнего запуска парсера;
- количество запросов;
- количество товаров;
- количество продавцов;
- количество ошибок сбора;
- полнота/частичность данных;
- топ запросов;
- топ продавцов по видимости;
- топ товаров по видимости;
- средняя/медианная/минимальная/максимальная цена;
- средний рейтинг;
- среднее количество отзывов;
- главные рыночные возможности;
- главные проблемы качества данных.

### 12.2. Query Analytics

По каждому запросу показывать:

- marketplace;
- query;
- normalized/canonical query, если есть;
- query group, если есть;
- source query;
- rank/priority/score;
- wordstat volume или аналог спроса, если подтверждено;
- количество найденных товаров;
- количество уникальных продавцов;
- среднюю/медианную/минимальную/максимальную цену;
- средний рейтинг;
- среднее количество отзывов;
- количество товаров в top-10/top-30/top-100;
- лидеров выдачи;
- competition_score;
- opportunity_score;
- data_quality_status.

Карточка запроса должна показывать товары по позициям, продавцов, ценовой коридор, распределения цен/рейтингов/отзывов, динамику и сигналы.

### 12.3. Product Analytics

По каждому товару показывать:

- marketplace;
- external_product_id;
- product name;
- brand;
- seller id/name;
- price/final_price/old_price/discount, если подтверждено;
- rating;
- reviews/feedbacks;
- promo markers;
- query_count;
- queries_found;
- best/avg/worst position;
- top-10/top-30/top-100 presence;
- visibility_score;
- first_seen_at;
- last_seen_at;
- is_new_in_period;
- is_lost_in_period;
- data_quality_status.

Карточка товара должна показывать продавца, бренд, цену, рейтинг, отзывы, все запросы, позиции, динамику позиции/цены/рейтинга/отзывов и похожие товары.

### 12.4. Seller Analytics

По каждому продавцу показывать:

- marketplace;
- external_seller_id;
- seller_name;
- seller_rating, если есть;
- seller reviews/feedbacks, если есть;
- количество найденных товаров;
- количество запросов;
- query groups;
- среднюю/лучшую позицию;
- долю присутствия в top-10/top-30/top-100;
- среднюю/минимальную/максимальную цену;
- динамику видимости;
- новые/пропавшие товары продавца;
- data_quality_status.

Карточка продавца должна показывать товары продавца, запросы, видимость по marketplace/query, ценовой диапазон, динамику и экспорт товаров продавца.

### 12.5. WB/Ozon comparison

Аналитика должна поддерживать сравнение маркетплейсов по сопоставимым query/query_group:

- наличие запроса на WB/Ozon;
- количество товаров;
- количество продавцов;
- медианная цена;
- минимальная/максимальная цена;
- средний рейтинг;
- среднее количество отзывов;
- competition_score;
- opportunity_score;
- наличие собственных товаров после подключения own-store данных.

Позиции WB и Ozon нельзя сравнивать напрямую как равнозначные значения. Нужно использовать нормализованные показатели:

```text
top_10_presence
top_30_presence
top_100_presence
visibility_score
price_index
competition_score
opportunity_score
```

### 12.6. История и динамика

Аналитика должна хранить историю запусков и показывать:

- изменение позиции товара;
- изменение цены;
- изменение рейтинга;
- изменение количества отзывов;
- новые/пропавшие товары;
- новые/пропавшие продавцы;
- изменение видимости продавца;
- изменение количества товаров в выдаче;
- изменение ценового коридора;
- изменение конкуренции по запросу.

### 12.7. Data Quality Dashboard

Отдельный раздел качества данных должен показывать:

- run_id;
- дата и время запуска;
- marketplace;
- статус: success / partial / failed;
- успешные и упавшие компоненты;
- количество обработанных запросов;
- количество страниц/порций;
- количество товаров;
- количество обогащённых продавцов;
- ошибки;
- частично собранные запросы;
- missing pages;
- можно ли использовать запуск в аналитике;
- data_confidence_level.

### 12.8. Поиск и фильтрация

Базовые фильтры:

- marketplace;
- период;
- run_id;
- query;
- query_group;
- product;
- external_product_id;
- seller;
- external_seller_id;
- brand;
- price range;
- rating range;
- reviews range;
- position range;
- only top-10/top-30/top-100;
- new products;
- lost products;
- own products после подключения own-store данных;
- competitor products;
- records with data quality issues.

Быстрый поиск:

- по названию товара;
- по ID товара;
- по продавцу;
- по запросу;
- по бренду.

### 12.9. Excel export

Excel-экспорт обязателен.

Минимальные выгрузки:

1. Запросы и метрики.
2. Товары по выбранному запросу.
3. Продавцы по выбранному запросу.
4. Все товары продавца.
5. Сравнение WB/Ozon.
6. Новые товары за период.
7. Пропавшие товары за период.
8. Изменение позиций.
9. Ценовой анализ.
10. Список рыночных возможностей.
11. Список проблем по собственным товарам после подключения own-store данных.

Требования к Excel-файлу:

- несколько листов для составных отчётов;
- понятные заголовки;
- автофильтры;
- дата формирования;
- marketplace;
- период;
- run_id / диапазон run_id;
- описание источника данных;
- предупреждение при partial data.

---

## 13. Будущие контуры аналитики

### 13.1. Own Store Intelligence

Должен быть заложен архитектурно, но реализация — отдельным этапом после подтверждения API-контрактов.

Потенциальные источники:

- WB Seller API;
- Ozon Seller API;
- Excel-выгрузки, если API не даёт нужные данные;
- внутренний справочник товаров.

Потенциальные данные:

- собственные товары;
- карточки;
- цены;
- скидки;
- остатки;
- заказы;
- продажи;
- возвраты, если доступны;
- акции;
- рекламные данные, если доступны;
- статусы товаров;
- склады;
- магазины/кабинеты.

### 13.2. Единый справочник товаров

Должна быть предусмотрена архитектура сущностей:

```text
product_master
marketplace_listing_map
```

`product_master`:

```text
internal_product_id
product_group
product_name
category
niche
production_type
cost_price, если доступна
target_margin, если доступна
is_active
```

`marketplace_listing_map`:

```text
internal_product_id
marketplace
store_id
external_product_id
wb_nm_id
ozon_product_id
ozon_offer_id
sku
listing_url
is_own_product
```

### 13.3. Decision Layer

Decision Layer должен быть спроектирован как будущий контур сигналов:

- высокий спрос + мало продавцов;
- высокий спрос + мало товаров;
- высокий спрос + слабые рейтинги лидеров;
- запрос есть в подсказках, но нет собственных товаров;
- собственный товар ниже top-100;
- собственный товар был в выдаче и пропал;
- цена собственного товара выше/ниже рынка;
- конкурент резко увеличил видимость;
- новый товар быстро вышел в top;
- товар есть на WB, но нет на Ozon, или наоборот;
- на одном маркетплейсе конкуренция ниже.

Рекомендации должны сопровождаться источником данных, объяснением и confidence level.

---

## 14. API аналитики

Минимальное функциональное покрытие backend API:

```text
GET /analytics/overview
GET /analytics/runs
GET /analytics/data-quality
GET /analytics/queries
GET /analytics/queries/{query_id}
GET /analytics/products
GET /analytics/products/{product_id}
GET /analytics/sellers
GET /analytics/sellers/{seller_id}
GET /analytics/marketplaces/compare
GET /analytics/signals
GET /analytics/export
```

Будущие own-store endpoints:

```text
GET /own/products
GET /own/listings
GET /own/prices
GET /own/stocks
GET /own/sales
GET /own/product/{internal_product_id}/market-position
```

Конкретные paths могут быть изменены при проектировании API, если функциональное покрытие сохранено.

---

## 15. Административный функционал

В архитектуре аналитики должен быть заложен admin-раздел:

- источники данных;
- настройки импорта;
- расписание обновлений;
- история импортов;
- ошибки импортов;
- подключение parser export;
- подключение WB API в будущем;
- подключение Ozon API в будущем;
- управление пользователями;
- роли и доступы;
- настройки Excel-экспорта;
- настройки сигналов;
- пороги opportunity_score;
- пороги competition_score;
- настройки предупреждений качества данных.

---

## 16. Веб-доступ и эксплуатация

### 16.1. Временный режим без домена

Рекомендуемые порты:

```text
market-parser-v2 web panel:      8092
market-parser-v2 MCP/debug:      8095, только если нужен и защищён
market-parser-v2 export/API:     8096
market-analytics web/API:        8090
```

Примеры:

```text
http://SERVER_IP:8092
http://SERVER_IP:8096/analytics-export/latest.json
http://SERVER_IP:8090
```

Требования:

- веб-панели должны иметь авторизацию;
- пароли по умолчанию должны быть заменены;
- secrets/cookies/API keys не должны показываться в UI;
- debug endpoints не должны быть открыты наружу без необходимости;
- export endpoint должен быть read-only.

### 16.2. Целевой режим

Целевая схема:

```text
Internet
  -> Nginx 80/443
    -> 127.0.0.1:8092 parser web
    -> 127.0.0.1:8096 parser export
    -> 127.0.0.1:8090 analytics web/API
```

Целевые адреса после появления домена:

```text
https://parser.domain.ru
https://analytics.domain.ru
```

Обязательно:

- HTTPS;
- HTTP -> HTTPS redirect;
- авторизация;
- ограничение debug endpoints;
- закрытие прямых внешних портов, кроме 80/443;
- логи доступа и ошибок;
- backup/restore конфигов и данных.

---

## 17. Безопасность

Запрещено:

- коммитить cookies;
- коммитить API keys;
- коммитить auth tokens;
- сохранять HAR/fixtures с секретами;
- логировать cookies и токены;
- отдавать секреты через UI или export bundle;
- смешивать WB и Ozon identifiers без marketplace/source_system;
- считать неподтверждённые финансовые метрики как факты.

Нужно предусмотреть:

- `.gitignore` для секретов, данных, логов и временных файлов;
- env-based конфигурацию secrets;
- sanitized samples;
- checksums для export bundle;
- user authentication;
- backup policy;
- data retention policy.

---

## 18. Этапы реализации продукта

### Этап 1. Source discovery и sample data

Результат:

- подтверждённая инвентаризация WB-парсера;
- подтверждённая инвентаризация Ozon-парсера;
- сверка Ozon docs vs code vs outputs;
- sample data без секретов;
- список подтверждённых полей, assumptions, gaps и risks.

### Этап 2. Data contracts и export contract

Результат:

- WB contract;
- Ozon contract;
- common marts contract;
- export bundle contract;
- schema versioning;
- data quality rules.

### Этап 3. `market-parser-v2` skeleton

Результат:

- чистый проект;
- core modules;
- provider abstraction;
- config;
- data paths to `markets_data`;
- CLI/API skeleton;
- tests skeleton;
- contract validation skeleton.

### Этап 4. Перенос/адаптация WB и Ozon логики

Результат:

- WB provider;
- Ozon provider;
- suggest/filter/serp/sellers;
- run reports;
- checkpoints;
- latest mirrors;
- export bundle.

### Этап 5. `market-analytics` skeleton

Результат:

- backend;
- database schema;
- import worker;
- parser export importer;
- checksum validation;
- imported run registry;
- basic auth;
- web skeleton.

### Этап 6. Market Intelligence MVP

Результат:

- overview;
- query analytics;
- product analytics;
- seller analytics;
- WB/Ozon comparison;
- data quality dashboard;
- Excel export.

### Этап 7. История и динамика

Результат:

- сравнение запусков;
- новые/пропавшие товары;
- новые/пропавшие продавцы;
- динамика цен, позиций, рейтингов, отзывов и видимости.

### Этап 8+. Future контуры

Отдельные этапы:

- API личных кабинетов WB/Ozon;
- справочник собственных товаров;
- product matching;
- Decision Layer;
- production hardening с доменом, HTTPS, мониторингом и backup.

---

## 19. Критерии приемки MVP

### 19.1. Parser MVP

`market-parser-v2` считается готовым для MVP, если:

- WB и Ozon работают через provider abstraction;
- исходные `wb-parser-v1` и `parser_ozon` не изменены;
- outputs пишутся в `markets_data`;
- есть `raw/staging/marts`;
- есть `source_system`/`marketplace` в контрактах;
- есть `run_id`, run reports, latest mirrors;
- есть export: `manifest`, `bundle`, `checksums`, `latest`;
- CSV совместимы с ожидаемым форматом;
- есть smoke tests;
- есть contract tests;
- нет cookies/secrets в Git, logs, fixtures или exports.

### 19.2. Analytics MVP

`market-analytics` считается готовой для MVP, если:

- импортирует export bundle через контракт;
- проверяет manifest и checksum;
- не читает внутренние папки парсера напрямую как основной режим;
- хранит imported run registry;
- поддерживает WB и Ozon через marketplace/source_system;
- показывает overview, queries, products, sellers, marketplace comparison и data quality;
- поддерживает историю запусков хотя бы на уровне imported runs;
- даёт Excel export;
- не превращает UI в одну огромную таблицу;
- имеет авторизацию;
- помечает partial/invalid data;
- не выводит неподтверждённые финансовые метрики как факты.

---

## 20. Основные риски

| Риск | Что делать |
|---|---|
| Ozon меняет frontend/widget structure | Использовать prefix matching, tests, fixtures, fallback extraction и clear failure states. |
| Ozon anti-bot / empty responses | Настраиваемые cookies, throttle, concurrency, stop/partial status, resume. |
| Seller data отсутствует в SERP Ozon | Использовать product-card HTML state enrichment, не искать seller в tileGrid. |
| WB и Ozon identifiers смешиваются | Всегда использовать marketplace/source_system в ключах и витринах. |
| Поля выдумываются без источника | Каждое поле контракта должно быть confirmed, assumption или future. |
| Analytics обещает прибыль/маржу без данных | Запретить такие метрики до подключения финансовых источников. |
| Partial runs воспринимаются как полные | Вводить data quality status и предупреждения в UI/export. |
| Export ломает импорт | Использовать manifest, schema_version, checksum и contract tests. |

---

## 21. Итоговое требование

Нужно получить жизнеспособный продукт, в котором:

1. новый объединённый парсер надёжно собирает внешний рынок WB/Ozon;
2. аналитика создаётся с нуля и импортирует данные только через стабильный контракт;
3. WB/Ozon данные не смешиваются без provider context;
4. пользователь видит не только таблицы, но и управленческие выводы;
5. качество данных явно показано;
6. будущие контуры own-store, product matching и decision layer заложены архитектурно, но не выдаются за реализованный функционал MVP.
