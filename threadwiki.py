import path,flask
import mistune as m
a,d=flask.Flask(""),path.Path("p")
@a.route("/<p>")
def s(p):
	f=d/p;k=f.text();f.write_text(flask.request.args.get('n', k));b=[f"[{l[2:]}](/{l[2:]})\n"for l in d.files()if"/"+p in l.text()]
	return m.markdown(f"#{p}\n{k}\n\n"+''.join(b))+f"<form><textarea name=n>{k}</textarea>\n<input type=submit>"