#!/usr/bin/env python3
import fitz
import argparse

def extract_region(pdf_path, page_num, x0, y0, x1, y1, output_path, zoom):
    doc = fitz.open(pdf_path)

    if page_num < 1 or page_num > len(doc):
        raise ValueError(f"ページ番号 {page_num} は有効範囲外です。PDFには {len(doc)} ページあります。")

    page = doc[page_num - 1]
    rect = fitz.Rect(x0, y0, x1, y1)
    matrix = fitz.Matrix(zoom, zoom)  # 解像度スケーリング
    pix = page.get_pixmap(clip=rect, matrix=matrix)

    pix.save(output_path)
    print(f"保存しました: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDFの特定領域を画像として抽出")
    parser.add_argument("pdf_path", help="PDFファイルのパス")
    parser.add_argument("--page", type=int, default=1, help="対象ページ番号（1始まり）")
    parser.add_argument("--x0", type=float, required=True, help="切り出す矩形の左上X座標")
    parser.add_argument("--y0", type=float, required=True, help="切り出す矩形の左上Y座標")
    parser.add_argument("--x1", type=float, required=True, help="切り出す矩形の右下X座標")
    parser.add_argument("--y1", type=float, required=True, help="切り出す矩形の右下Y座標")
    parser.add_argument("--out", default="region.png", help="出力画像ファイル名")
    parser.add_argument("--zoom", type=float, default=1.0, help="スケーリング倍率（例: 2.0で2倍解像度）")

    args = parser.parse_args()
    extract_region(args.pdf_path, args.page, args.x0, args.y0, args.x1, args.y1, args.out, args.zoom)
