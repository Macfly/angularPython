import { Component, OnDestroy, OnInit } from '@angular/core';
import { SocketService } from '../socket.service';
import { Subscription } from 'rxjs';
import { Stock } from '../model/stockModel';

@Component({
  selector: 'app-socket-price',
  templateUrl: './socket-price.component.html',
  styleUrls: ['./socket-price.component.css']
})
export class SocketPriceComponent implements OnInit, OnDestroy {

  public stock = new Stock();
  public sub: Subscription;

  constructor(private socketService: SocketService) {

  }

  ngOnInit() {
    // this.sub = this.socketService.getQuotes()
    //   .subscribe(stock => {
    //     this.stock = stock;
    //     console.log(this.stock);
    //   });
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
