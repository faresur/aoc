import Data.List
import Data.List.Split

splitToInts :: String -> [Int]
splitToInts str = map (read::String->Int) $ words str

firstList :: [[Int]] -> [Int]
firstList xs = map head $ xs

secondList :: [[Int]] -> [Int]
secondList xs = map last $ xs

diffSum :: [(Int, Int)] -> Int
diffSum xs = foldl (\a b -> a + (abs $ (fst b) - (snd b))) 0 xs

pairAscending :: [Int] -> [Int] -> [(Int, Int)]
pairAscending xs ys = zip (sort xs) (sort ys)

count :: Int -> [Int] -> Int
count n xs = length $ filter (n==) xs

multByOccurences :: [Int] -> [Int] -> [Int]
multByOccurences xs ys = map (\x -> x * count x ys) xs

main :: IO ()
main = do 
  puzzleInput <- getContents
  let input = map splitToInts $ lines puzzleInput
  let first = firstList input
  let second = secondList input
  putStr "Part 1 answer: "
  print $ diffSum $ pairAscending first second
  putStr "Part 2 answer: "
  print $ sum $ multByOccurences first second
