import { Component } from '@angular/core';

@Component({
  selector: 'app-radio-editor',
  templateUrl: './radio-editor.component.html',
  styleUrls: ['./radio-editor.component.css']
})
export class RadioEditorComponent {
  question_text: string = 'Texto da pergunta';
  selected_option: string = '';
  options: any[] = [
    { "text": 'Option 1' },
    { "text": 'Option 2' },
    { "text": 'Option 3' },
  ];
}
