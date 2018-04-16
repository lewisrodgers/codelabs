import { Component, OnInit } from '@angular/core';
import { Unit } from '../unit';
import { UNITS } from '../units';

@Component({
  selector: 'app-calculator',
  templateUrl: './calculator.component.html',
  styleUrls: ['./calculator.component.css']
})
export class CalculatorComponent implements OnInit {
  units = UNITS;

  selectedUnit: Unit;

  constructor() { }

  ngOnInit() {
  }

  onSelect(unit: Unit) {
    this.selectedUnit = unit;
  }

}
