export class Stock {
  symbol: string;
  open: number;
  last: number;
  high: number;
  low: number;
  change: number;

  constructor() {
    this.change = 0;
    this.high = 0;
    this.last = 0;
    this.low = 0;
    this.open = 0;
    this.symbol = '';
  }
}
