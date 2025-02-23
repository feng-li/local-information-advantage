# Stock Forum Data Cleaning

## Data Description

1. There are two databases currently on the server. The first is located at `/home1/yqhuang/sentiment_out/` and contains posts, while the other is in a MySQL database. Both databases share common data such as stock information (e.g., `Id`, `reply`, `floor`). The main difference is that the first database also includes **sentiment scores** of the posts and **geographical information** for both the poster and the company (e.g., posterprov, firmprov). The second database contains the specific content of each post.

2. The `post` folder stores **8660 posts** with high reply volumes and sentiment scores, similar to a post on Baidu Tieba, where each post is initiated by the original poster and followed by replies from others. This set of posts was obtained from the stock forum data retrieval, though it is limited by strict selection criteria, resulting in a small sample size.

## Issues Encountered

- **Corrupted Data**: A total of 293 posts in MySQL are corrupted and cannot be properly read from the SQL database. The majority of these are from mid- and small-cap stocks.

- **Missing Geographic Information**: The SQL database only contains the content of posts and lacks regional information. Merging the data with results from `yqhuang` for region-based matching is unavoidable.

- **Post Counts**: In the original dataset, there are 759 posts from small and medium boards, 457 from the ChiNext, 511 from Shenzhen, and 935 from Shanghai. In the newly exported data from SQL, the counts are 397, 355, 472, and 945, respectively. This discrepancy suggests two different data extraction methods were used. We will use the original dataset as the reference for post count and use the `post` folder data for keyword search.

## Processing Approach

1. **Keyword Extraction**: Extract keywords from posts that may contain insider information. These will form a keyword list.

   - **Manual Search Scope**: Posts in the `post` folder that are **region-matched** and have more than 200 replies.

   - If the keyword list does not yield satisfactory results, remove the **reply count** and **region match** restrictions one by one to expand the search scope.

   - Required function: `get_post(n)`, where $\pmb{n} \in [0, 8659]$, is used to view the nth post in the `post` folder.

2. **Manual Classification of Posts**: Manually classify posts that are suspected of revealing insider information.

   - Use a dictionary to store the posts, with the **key** being `<name>_<Id>`, and the **value** being the content of that post.

   - Required function: `append_post(dict, name, id)`, where `dict` is the dictionary, `name` is the post name, and `id` is the post's ID.

3. **Stock Price Prediction**: Check if the predictions align with the **positive or negative impacts** determined in step 2.

   - For each post, download the Wind data for the 28 days before and 7 days after the post date, excluding weekends.

   - Use the **auto-arima** model to predict stock price movements for the next 7 days.

   - Perform a **K-test** and check if the prediction aligns with the actual trend.

   - Manually classify the predicted stock trend as either **positive** or **negative** and record the results.

   - Required functions:
     - `download_wind(value)`: Downloads the Wind data for each post. Exclude weekend data and save it as `<name>_<Id>`.
     - `wind_forecast(name)`: Predicts the stock price trend based on the downloaded data, performs the K-test, and visualizes the results.
     - `write_result(dict, name)`: Records the final results in two dictionaries, **positive** and **negative**, based on the analysis. The key format is `<name>_<Id>`.

## Processing Results

- There are **312,977,361** replies across four stock boards under the path `/home1/yqhuang/sentiment_out/`, with **14,831,134** posts (4.73% of the total posts) where the poster’s city matches the company’s city.

- We selected the **4 most extreme sentiment posts** (2 with the highest sentiment and 2 with the lowest) from each stock forum, resulting in **8660 posts** with a total of **4,598,768 replies** (1.5%). Among them, **209,046** posts have a matching geographical region, and **198,823** posts have both region matching and more than 200 replies.

- We applied keyword filtering (keywords: '内部', '内幕', '内部消息', '内幕消息', '透露', '偷偷') to posts with **region matching** and **more than 200 replies**, yielding **690** replies.

- After removing duplicate posts within the same stock on the same day, we ended up with **476** valid replies.

- We downloaded Wind data for the 28 days before and 7 days after the post dates, excluding weekends, and used Python's **auto-arima** function to forecast stock price movements. We manually classified the posts into **positive** or **negative** information.

- The manual classification resulted in **34** posts categorized as **positive** (bullish) and **23** as **negative** (bearish).
