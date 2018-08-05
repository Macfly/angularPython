import { Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { Stock } from '../model/stockModel';
import { Subscription } from 'rxjs';
import { SocketService } from '../socket.service';
import { MatTable } from '@angular/material';

@Component({
  selector: 'app-stock-table',
  templateUrl: './stock-table.component.html',
  styleUrls: ['./stock-table.component.css']
})
export class StockTableComponent implements OnInit, OnDestroy {
  displayedColumns: string[] = ['symbol', 'open', 'last', 'change', 'high', 'low', 'unwatch'];
  stocks: Stock[] = [];
  stocksPsition: { [id: string]: number; } = {};
  public sub: Subscription;
  @ViewChild(MatTable) table: MatTable<any>;

  constructor(private socketService: SocketService) {
  }

  ngOnInit() {
    this.sub = this.socketService.getQuotes()
      .subscribe(stock => {
        const position = this.stocks.findIndex((quoteEl: Stock) => {
          return quoteEl.symbol === stock.symbol;
        });
        if (position < 0) {
          this.stocks.push(stock);
        } else {
          this.stocks[position] = stock;
        }
        this.table.renderRows();
      });
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }

  onRemoveStock(stock: string) {
    this.socketService.unwatchStock(stock);
    const position = this.stocks.findIndex((quoteEl: Stock) => {
      return quoteEl.symbol === stock;
    });
    if (position > -1) {
      this.stocks.splice(position, 1);
      this.table.renderRows();
    }
  }
}
