## if
Syntax of if:

<table border="0" cellpadding="1" cellspacing="1" style="background-color:#2c3e50; border-radius:10px; border:2px solid ; outline:none; border: 0px;">
	<tbody>
		<tr>
			<td>
                <p></p>
                <p><span style="color:#9b59b6">if </span><span style="color:#e67e22">Condition</span><span style="color:#9b59b6">&nbsp;then</span></p>
                <p><span style="color:#95a5a6">&nbsp; &nbsp; #Code</span></p><p><span style="color:#9b59b6">end</span></p>
			</td>
		</tr>
	</tbody>
</table>

```Condition``` can be:

Equals: ```a == b```

Not Equals: ```a != b```

Less than: ```a < b```

Less than or equal to: ```a <= b```

Greater than: ```a > b```

Greater than or equal to: ```a >= b```

or any Function or Variable that Return ```True``` or ```1```
like the ```True``` Variable Because ```True``` Variable always Have the Value of 1

Example:
<table border="0" cellpadding="1" cellspacing="1" style="background-color:#2c3e50; border-radius:10px; border:2px solid ; outline:none; border: 0px;">
	<tbody>
		<tr>
			<td>
                <p></p>
                <p><span style="color:#9b59b6">if 2 </span><span style="color:#e67e22">==</span><span style="color:#9b59b6">&nbsp;2 then</span></p>
                <p><span style="color:#27ae60">&nbsp; &nbsp; print(<span style="color:#3498db">&nbsp;"2 Equals 2"</span>)</span></p><p><span style="color:#9b59b6">end</span>
                </p><p>
                <span style="color:#9b59b6">if not 2 </span><span style="color:#e67e22">==</span><span style="color:#9b59b6">&nbsp;2 then</span></p>
                <p></p>
                <p><span style="color:#27ae60">&nbsp; &nbsp; print(<span style="color:#3498db">&nbsp;"2 is not Equals 2"</span>)</span></p><p><span style="color:#9b59b6">end</span></p>
			</td>
		</tr>
	</tbody>
</table>

output:

<table border="0" cellpadding="1" cellspacing="1" 
style="background-color:#2c3e50; border-radius:10px; border:2px solid ; outline:none; border: 0px;">
	<tbody>
		<tr>
			<td>
                <p></p>
				<p>2 Equals 2</p>
			</td>
		</tr>
	</tbody>
</table>

```print("2 is not Equals 2")``` Never runs Because 2 can't not be 2
## for

Syntax:

<table border="0" cellpadding="1" cellspacing="1" 
style="background-color:#2c3e50; border-radius:10px; border:2px solid ; outline:none; border: 0px;">
	<tbody>
		<tr>
			<td>
                <p></p>
				<p><span style="color:#9b59b6">for</span> <span style="color:#e67e22">for_variable</span> = <span style="color:#e67e22">start</span><span style="color:#9b59b6"> to </span><span style="color:#e67e22">end_for </span><span style="color:#9b59b6">then</span></p>
				<p>&nbsp; &nbsp; <span style="color:#27ae60">print(</span><span style="color:#e67e22">i</span><span style="color:#27ae60">)</span></p>
				<p><span style="color:#9b59b6">end</span></p>
			</td>
		</tr>
	</tbody>
</table>

Example:

<table border="0" cellpadding="1" cellspacing="1" 
style="background-color:#2c3e50; border-radius:10px; border:2px solid ; outline:none; border: 0px;">
	<tbody>
		<tr>
			<td>
                <p></p>
				<p><span style="color:#9b59b6">let </span>start_for = <span style="color:#9b59b6">0</span></p>
				<p><span style="color:#9b59b6">let </span>end_for = <span style="color:#9b59b6">5</span></p>
				<p><span style="color:#9b59b6">for</span> <span style="color:#e67e22">i</span> = <span style="color:#e67e22">start</span><span style="color:#9b59b6"> to </span><span style="color:#e67e22">end_for </span><span style="color:#9b59b6">then</span></p>
				<p>&nbsp; &nbsp; <span style="color:#27ae60">print(</span><span style="color:#e67e22">i</span><span style="color:#27ae60">)</span></p>
				<p><span style="color:#9b59b6">end</span></p>
			</td>
		</tr>
	</tbody>
</table>

output:

<table border="0" cellpadding="1" cellspacing="1" 
style="background-color:#2c3e50; border-radius:10px; border:2px solid ; outline:none; border: 0px;">
	<tbody>
		<tr>
			<td>
                <p></p>
				<p>0<br>
				1<br>
				2<br>
				3<br>
				4</p>
			</td>
		</tr>
	</tbody>
</table>