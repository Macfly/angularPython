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

@NgModule({
  declarations: [
    AppComponent,
    RestPriceComponent,
    SocketPriceComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule
  ],
  providers: [SocketService, RestService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
