import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Stock } from './model/stockModel';

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};

const SERVER_URL = 'http://localhost:5000';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http: HttpClient) {
  }

  getStockPrice(): Observable<Stock> {
    return this.http.get<Stock>(SERVER_URL + '/api/market/GE');
  }

  postStockPrice(stock: string): Observable<Stock> {
    return this.http.post<Stock>(SERVER_URL + '/api/market', {'stock': stock}, httpOptions);
  }
}
