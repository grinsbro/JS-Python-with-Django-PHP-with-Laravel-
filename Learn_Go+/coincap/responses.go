package coincap

import "fmt"

type AssetsResponse struct {
	Data      []Asset `json:"data"`
	TimeStamp int64   `json:"timestamp"`
}

type AssetResponse struct {
	Data      Asset `json:"data"`
	TimeStamp int64 `json:"timestamp"`
}

type Asset struct {
	ID           string `json:"id"`
	Rank         string `json:"rank"`
	Symbol       string `json:"symbol"`
	Name         string `json:"name"`
	Supply       string `json:"supply"`
	MaxSupply    string `json:"maxSupply"`
	MarketCapUSD string `json:"marketCapUsd"`
	VolumeUSD24h string `json:"volumeUsd24Hr"`
	PriceUSD     string `json:"priceUsd"`
}

func (d Asset) Info() string {
	return fmt.Sprintf("[ID] %s | [Rank] %s | [Symbol] %s | [Name] %s | [Price] %s", d.ID, d.Rank, d.Symbol, d.Name, d.PriceUSD)
}
