Sub RemoveProgressBar()
    On Error Resume Next
        With ActivePresentation
              For i = 1 To .Slides.Count
              .Slides(i).Shapes("PBB").Delete
              .Slides(i).Shapes("PBF").Delete
              Next i:
        End With
End Sub
