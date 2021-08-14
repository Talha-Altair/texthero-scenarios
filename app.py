import texthero as hero
import pandas as pd

df = pd.read_csv(
   "data.csv"
)

df['pca'] = (
   df['text']
   .pipe(hero.clean)
   .pipe(hero.tfidf)
   .pipe(hero.pca)
)

# hero.scatterplot(df, 'pca', color='topic', title="PCA BBC Sport news")

print(df)