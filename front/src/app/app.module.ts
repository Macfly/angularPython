import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { RestPriceComponent } from './rest-price/rest-price.component';
import { SocketPriceComponent } from './socket-price/socket-price.component';
import { SocketService } from './socket.service';
import { RestService } from './rest.service';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material/material.module';
import { StockInputComponent } from './stock-input/stock-input.component';
import { StockTableComponent } from './stock-table/stock-table.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    RestPriceComponent,
    SocketPriceComponent,
    StockInputComponent,
    StockTableComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule,
    FormsModule
  ],
  providers: [SocketService, RestService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
