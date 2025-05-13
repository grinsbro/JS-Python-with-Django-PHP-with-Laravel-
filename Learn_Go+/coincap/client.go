package coincap

import (
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"os"
	"time"
)

type Client struct {
	client *http.Client
}

func NewClient(timeout time.Duration) (*Client, error) {
	if timeout == 0 {
		return nil, errors.New("TIMEOUT CAN'T BE 0")
	}
	return &Client{
		client: &http.Client{
			Timeout: timeout,
			Transport: &loggingRoundTripper{
				logger: os.Stdout,
				next:   http.DefaultTransport,
			},
		},
	}, nil
}

func (c Client) GetAssets() ([]Asset, error) {
	resp, err := c.client.Get("https://rest.coincap.io/v3/assets?apiKey=b61e73808e48c1885a67af8e7a94b6cbfba8b21e08e35d940737813f4275cdbc")
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}
	var r AssetsResponse
	err = json.Unmarshal(body, &r)
	if err != nil {
		return nil, err
	}

	return r.Data, nil
}
