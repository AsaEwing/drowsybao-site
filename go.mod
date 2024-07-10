module github.com/nicokaiser/hugo-gallery-starter

go env -w GO111MODULE=auto

go 1.20

go mod init

require github.com/nicokaiser/hugo-theme-gallery/v4 v4.0.0 // indirect

replace github.com/nicokaiser/hugo-theme-gallery/v4 => ../
