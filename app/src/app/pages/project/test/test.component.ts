import {Component} from "@angular/core";

@Component({
  selector: 'test',
  styleUrls: ['./test.component.scss'],
  template: `
    <div class="pms-main"><router-outlet></router-outlet></div>`
})
export class TestComponent {}
