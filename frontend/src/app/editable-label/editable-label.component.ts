import { Component, Input, Output, EventEmitter } from '@angular/core';
import { A11yModule } from '@angular/cdk/a11y' // autofocus used in the template (check if it should be included in app.module.ts)  

@Component({
  selector: 'app-editable-label',
  templateUrl: './editable-label.component.html',
  styleUrls: ['./editable-label.component.css']
})
export class EditableLabelComponent {
  // appropriate names are necessary for two way data binding. 
  // see https://angular.io/guide/two-way-binding
  @Input() text = 'Click to edit';
  @Input() canRemove = true;
  @Output() textChange = new EventEmitter<string>();
  @Output() onRemove = new EventEmitter<string>();

  isEditing = false;

  onSubmit() {
    this.textChange.emit(this.text);
    this.isEditing = false;
  }

  toggleEditing() {
    this.isEditing = !this.isEditing;
  }

  handleRemoveClick() {
    this.onRemove.emit(this.text);
  }
}
