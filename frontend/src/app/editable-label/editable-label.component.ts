import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-editable-label',
  templateUrl: './editable-label.component.html',
  styleUrls: ['./editable-label.component.css']
})
export class EditableLabelComponent {
  // appropriate names are necessary for two way data binding. 
  // see https://angular.io/guide/two-way-binding
  @Input() text = 'Label';
  @Output() textChange = new EventEmitter<string>();

  isEditing = false;

  onSubmit() {
    console.log("text: " + this.text);
    this.textChange.emit(this.text);
    this.isEditing = false;
  }

  toggleEditing() {
    this.isEditing = !this.isEditing;
  }
}
