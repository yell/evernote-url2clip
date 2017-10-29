Sub AddProgressBar()
    On Error Resume Next
    With ActivePresentation
        For i = 1 To .Slides.Count
             .Slides(i).Shapes("PBB").Delete ' remove previous
             .Slides(i).Shapes("PBF").Delete

            Set t = .Slides(i).Shapes.AddShape(msoShapeRectangle, _
            0, .PageSetup.SlideHeight - 12, _
            .PageSetup.SlideWidth, 12)
            t.Fill.ForeColor.RGB = RGB(220, 220, 220) ' change bg color
            t.Line.Visible = False ' remove std line
            t.Name = "PBB"

            Set s = .Slides(i).Shapes.AddShape(msoShapeRectangle, _
            0, .PageSetup.SlideHeight - 12, _
            i * .PageSetup.SlideWidth / .Slides.Count, 12)

            s.Fill.ForeColor.RGB = RGB(50, 50, 50) ' change moving color here
            s.Line.Visible = False ' remove std line
            s.Name = "PBF"
            Next i:
    End With
End Sub
