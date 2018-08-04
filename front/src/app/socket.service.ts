import { Injectable } from '@angular/core';
import { Observable, Observer } from 'rxjs';

import * as socketio from 'socket.io-client';
import { Stock } from './model/stockModel';

const SERVER_URL = 'http://localhost:5000';
const connections = {'transports': ['websocket']};

@Injectable()
export class SocketService {
  public socket;
  public observer: Observer<Stock>;

  getQuotes(): Observable<Stock> {
    this.socket = socketio(SERVER_URL, connections);
    this.socket.emit('join', 'GM');

    this.socket.on('stock', (res) => {
      this.observer.next(res);
    });

    return this.createObservable();
  }

  createObservable(): Observable<Stock> {
    return new Observable(observer => {
      this.observer = observer;
    });
  }
}
