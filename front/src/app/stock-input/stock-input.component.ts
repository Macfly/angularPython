import { Component, OnInit } from '@angular/core';
import { SocketService } from '../socket.service';

@Component({
  selector: 'app-stock-input',
  templateUrl: './stock-input.component.html',
  styleUrls: ['./stock-input.component.css']
})
export class StockInputComponent implements OnInit {

  constructor(private socketService: SocketService) {
  }

  ngOnInit() {
  }

  onAddStock(stock: string) {
    this.socketService.watchStock(stock);
  }
}
