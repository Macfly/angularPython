import { Component, OnInit } from '@angular/core';
import { RestService } from '../rest.service';
import { Stock } from '../model/stockModel';

@Component({
  selector: 'app-rest-price',
  templateUrl: './rest-price.component.html',
  styleUrls: ['./rest-price.component.css']
})
export class RestPriceComponent implements OnInit {

  public stockGet = new Stock();
  public stockPost = new Stock();

  constructor(private restService: RestService) {

  }

  ngOnInit() {
  }

  onRefreshGet() {
    this.restService.getStockPrice()
      .subscribe(price => {
        this.stockGet = price;
        console.log(this.stockGet);
      });
  }

  onRefreshPost() {
    this.restService.postStockPrice('JPM')
      .subscribe(price => {
        this.stockPost = price;
        console.log(this.stockPost);
      });
  }
}
