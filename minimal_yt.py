from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
db = SQLAlchemy(app)

# Model

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"


# names = {"tim": {"age": "19", "gender": "male"},
#         "Manan": {"age":"23", "gender": "male"}}

# class HelloWorld(Resource):
#     def get(self, name):
#         return names[name]
#
#     def post(self):
#         return {"Data": "Posted"}

# api.add_resource(HelloWorld, "/helloworld/<string:name>")

videos = {}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_update_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_update_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

# def abort_if_null_video_id(video_id):
#     if video_id not in videos:
#         abort(404, "Video id is not valid...")
#
# def abort_if_video_exists(video_id):
#     if video_id in videos:
#         abort(409, "Video already exists with that ID...")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        if not self.check_if_video_exists(video_id):
            abort(404, "Could not find video with that id")
        return result

    def put(self, video_id):
        args = video_put_args.parse_args()
        if self.check_if_video_exists(video_id):
            abort(409, "Video id taken...")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return args, 201

    def delete(self, video_id):
        abort_if_null_video_id(video_id)
        del videos[video_id]
        return '', 204

    def check_if_video_exists(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            return result
        else:
            return False

    def patch(self, video_id):
        args = video_put_args.parse_args()
        result = self.check_if_video_exists(video_id)
        if not result:
            abort(404, "Video does not exist!")
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result

api.add_resource(Video, "/video/<int:video_id>")





if __name__ == "__main__":
    app.run(debug=True)

